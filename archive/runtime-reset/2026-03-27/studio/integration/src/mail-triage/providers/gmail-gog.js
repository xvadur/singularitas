import { runCommand } from '../lib/command.js';

function parseJson(stdout) {
  if (!stdout?.trim()) {
    return null;
  }
  return JSON.parse(stdout);
}

export class GmailGogProvider {
  constructor({ account }) {
    this.account = account;
  }

  async searchThreads({ query, maxResults }) {
    const args = [
      '-a',
      this.account,
      'gmail',
      'search',
      '--json',
      '--results-only',
      `--max=${maxResults}`,
      query
    ];

    const { stdout } = await runCommand('gog', args);
    return parseJson(stdout) || [];
  }

  async getThread(threadId) {
    const args = [
      '-a',
      this.account,
      'gmail',
      'thread',
      'get',
      '--json',
      '--results-only',
      threadId
    ];

    const { stdout } = await runCommand('gog', args);
    const result = parseJson(stdout);
    return result?.thread ?? result;
  }

  async ensureLabel(labelName) {
    const listArgs = ['-a', this.account, 'gmail', 'labels', 'list', '--json', '--results-only'];
    const { stdout } = await runCommand('gog', listArgs);
    const labels = parseJson(stdout) || [];
    const existing = labels.find((item) => item.name === labelName);
    if (existing) {
      return existing;
    }

    const createArgs = ['-a', this.account, 'gmail', 'labels', 'create', '--json', '--results-only', labelName];
    const created = await runCommand('gog', createArgs);
    return parseJson(created.stdout);
  }

  async modifyThreadLabels(threadId, { add = [], remove = [] }) {
    const args = ['-a', this.account, 'gmail', 'thread', 'modify', '--json', '--results-only', threadId];
    if (add.length > 0) {
      args.push('--add', add.join(','));
    }
    if (remove.length > 0) {
      args.push('--remove', remove.join(','));
    }

    const { stdout } = await runCommand('gog', args);
    return parseJson(stdout);
  }

  async createDraft({ to, subject, body, replyToMessageId }) {
    const args = [
      '-a',
      this.account,
      'gmail',
      'drafts',
      'create',
      '--json',
      '--results-only',
      '--to',
      to,
      '--subject',
      subject,
      '--body',
      body
    ];

    if (replyToMessageId) {
      args.push('--reply-to-message-id', replyToMessageId);
    }

    const { stdout } = await runCommand('gog', args);
    return parseJson(stdout);
  }
}
