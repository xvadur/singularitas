#!/usr/bin/env node
import path from 'node:path';
import { loadConfig, resolveMailboxConfig } from './lib/config.js';
import { parseArgs } from './lib/utils.js';
import { runMailboxTriage } from './run.js';

async function main() {
  const args = parseArgs(process.argv.slice(2));
  const workspaceDir = process.cwd();
  const configPath = path.resolve(workspaceDir, args.config || 'config/mail-triage.sample.json');
  const mailboxName = args.mailbox || 'business';

  const config = await loadConfig(configPath);
  const mailboxConfig = resolveMailboxConfig(config, mailboxName);
  const mode = args.mode || config.defaultMode || 'dry-run';

  if (!['dry-run', 'apply'].includes(mode)) {
    throw new Error(`Unsupported mode '${mode}'. Use dry-run or apply.`);
  }

  const report = await runMailboxTriage({
    workspaceDir,
    config,
    mailboxName,
    mailboxConfig,
    mode
  });

  const summary = {
    runId: report.runId,
    mailbox: report.mailboxName,
    account: report.mailboxAccount,
    mode: report.mode,
    fetched: report.counts.threadsFetched,
    draftsPlanned: report.counts.draftsPlanned,
    draftsCreated: report.counts.draftsCreated,
    categories: report.items.reduce((accumulator, item) => {
      const key = item.classification.category;
      accumulator[key] = (accumulator[key] || 0) + 1;
      return accumulator;
    }, {})
  };

  console.log(JSON.stringify(summary, null, 2));
}

main().catch((error) => {
  console.error(error.message);
  process.exitCode = 1;
});
