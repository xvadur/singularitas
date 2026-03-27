import { decodeBase64Url, htmlToText, pickHeader, truncate } from './utils.js';

function extractTextFromPayload(payload) {
  if (!payload) {
    return '';
  }

  const mimeType = payload.mimeType || '';
  const directBody = decodeBase64Url(payload.body?.data || '');

  if (mimeType.includes('text/plain') && directBody) {
    return directBody;
  }

  if (mimeType.includes('text/html') && directBody) {
    return htmlToText(directBody);
  }

  for (const part of payload.parts || []) {
    const text = extractTextFromPayload(part);
    if (text) {
      return text;
    }
  }

  if (directBody) {
    return directBody;
  }

  return '';
}

export function normalizeThread(threadSummary, threadDetail) {
  const messages = threadDetail?.messages || [];
  const latestMessage = messages[messages.length - 1] || {};
  const headers = latestMessage.payload?.headers || [];
  const bodyText = extractTextFromPayload(latestMessage.payload);

  return {
    threadId: threadDetail.id || threadSummary.id,
    messageId: latestMessage.id,
    subject: pickHeader(headers, 'Subject') || threadSummary.subject || '',
    from: pickHeader(headers, 'From') || threadSummary.from || '',
    to: pickHeader(headers, 'To') || '',
    deliveredTo: pickHeader(headers, 'Delivered-To') || '',
    date: pickHeader(headers, 'Date') || threadSummary.date || '',
    labels: [...new Set([...(threadSummary.labels || []), ...(latestMessage.labelIds || [])])],
    snippet: latestMessage.snippet || '',
    bodyText: truncate(bodyText || latestMessage.snippet || '', 5000),
    messageCount: messages.length || threadSummary.messageCount || 1,
    raw: {
      summary: threadSummary,
      latestMessageHeaders: headers
    }
  };
}
