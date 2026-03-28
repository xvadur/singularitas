import path from 'node:path';
import { GmailGogProvider } from './providers/gmail-gog.js';
import { normalizeThread } from './lib/normalize.js';
import { classifyMessage } from './lib/classifier.js';
import { buildActionPlan } from './lib/planner.js';
import { createDraftReply } from './lib/draft-reply.js';
import { ensureDir, nowStamp, writeJson } from './lib/utils.js';

function makeProvider(mailboxConfig) {
  if (mailboxConfig.provider?.type !== 'gmail-gog') {
    throw new Error(`Unsupported provider type '${mailboxConfig.provider?.type}'.`);
  }

  return new GmailGogProvider({ account: mailboxConfig.account });
}

export async function runMailboxTriage({ workspaceDir, config, mailboxName, mailboxConfig, mode }) {
  const provider = makeProvider(mailboxConfig);
  const startedAt = new Date().toISOString();
  const runId = `${mailboxName}-${nowStamp()}`;

  const requiredLabels = [
    mailboxConfig.labels.processed,
    mailboxConfig.labels.needsReply,
    mailboxConfig.labels.awaitingHuman,
    ...Object.values(mailboxConfig.labels.categories)
  ];

  if (mode === 'apply') {
    for (const label of requiredLabels) {
      await provider.ensureLabel(label);
    }
  }

  const threadSummaries = await provider.searchThreads({
    query: mailboxConfig.fetch.query,
    maxResults: mailboxConfig.fetch.maxResults
  });

  const items = [];

  for (const summary of threadSummaries) {
    const detail = await provider.getThread(summary.id);
    const normalized = normalizeThread(summary, detail);
    const classification = await classifyMessage({
      aiConfig: config.ai,
      mailboxConfig,
      message: normalized
    });
    const plan = buildActionPlan({ mailboxConfig, message: normalized, classification });

    const item = {
      threadId: normalized.threadId,
      messageId: normalized.messageId,
      normalized,
      classification,
      plan,
      execution: {
        mode,
        labelsApplied: false,
        draftCreated: false
      }
    };

    if (plan.shouldDraftReply) {
      try {
        item.proposedDraft = await createDraftReply({
          aiConfig: config.ai,
          mailboxConfig,
          message: normalized,
          classification
        });
      } catch (error) {
        item.proposedDraft = { error: error.message };
      }
    }

    if (mode === 'apply') {
      await provider.modifyThreadLabels(normalized.threadId, {
        add: plan.addLabels,
        remove: plan.removeLabels
      });
      item.execution.labelsApplied = true;

      if (plan.shouldDraftReply && item.proposedDraft && !item.proposedDraft.error && !item.proposedDraft.skipped) {
        item.execution.draft = await provider.createDraft({
          to: item.proposedDraft.to,
          subject: item.proposedDraft.subject,
          body: item.proposedDraft.body,
          replyToMessageId: normalized.messageId
        });
        item.execution.draftCreated = true;
      }
    }

    items.push(item);
  }

  const report = {
    runId,
    mailboxName,
    mailboxAccount: mailboxConfig.account,
    mode,
    startedAt,
    finishedAt: new Date().toISOString(),
    fetchQuery: mailboxConfig.fetch.query,
    counts: {
      threadsFetched: threadSummaries.length,
      draftsPlanned: items.filter((item) => item.plan.shouldDraftReply).length,
      draftsCreated: items.filter((item) => item.execution.draftCreated).length
    },
    items
  };

  const runsDir = path.join(workspaceDir, 'runs', 'mail-triage');
  await ensureDir(runsDir);
  await writeJson(path.join(runsDir, `${runId}.json`), report);

  return report;
}
