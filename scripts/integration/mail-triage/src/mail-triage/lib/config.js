import { readFile } from 'node:fs/promises';

export async function loadConfig(configPath) {
  const raw = await readFile(configPath, 'utf8');
  return JSON.parse(raw);
}

export function resolveMailboxConfig(config, mailboxName) {
  const mailbox = config?.mailboxes?.[mailboxName];
  if (!mailbox) {
    throw new Error(`Mailbox '${mailboxName}' not found in config.`);
  }
  return mailbox;
}
