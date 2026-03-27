function inferRecipient(fromHeader) {
  const match = String(fromHeader).match(/<([^>]+)>/);
  return match ? match[1] : String(fromHeader).trim();
}

function subjectLine(subject) {
  return /^re:/i.test(subject) ? subject : `Re: ${subject}`;
}

export async function createDraftReply({ aiConfig, mailboxConfig, message, classification }) {
  const apiKey = process.env[aiConfig.apiKeyEnv];
  const recipient = inferRecipient(message.from);

  if (!apiKey) {
    return {
      skipped: true,
      reason: `Missing AI API key in env ${aiConfig.apiKeyEnv}.`
    };
  }

  const response = await fetch(`${aiConfig.baseUrl}/chat/completions`, {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      authorization: `Bearer ${apiKey}`
    },
    body: JSON.stringify({
      model: aiConfig.model,
      temperature: 0.3,
      response_format: { type: 'json_object' },
      messages: [
        {
          role: 'system',
          content: 'Draft concise business email replies. Output JSON only. Never claim the email has already been sent.'
        },
        {
          role: 'user',
          content: JSON.stringify({
            task: 'Draft a reply for human review only.',
            category: classification.category,
            guidance: classification.draftReplyInstructions || 'Acknowledge receipt, be concise, and leave room for Adam to personalize.',
            email: {
              from: message.from,
              subject: message.subject,
              snippet: message.snippet,
              bodyText: message.bodyText.slice(0, 4000)
            },
            output: {
              subject: subjectLine(message.subject),
              body: 'plain text only'
            }
          })
        }
      ]
    })
  });

  if (!response.ok) {
    const body = await response.text();
    throw new Error(`Draft generation failed (${response.status}): ${body}`);
  }

  const payload = await response.json();
  const content = JSON.parse(payload?.choices?.[0]?.message?.content || '{}');
  const signature = mailboxConfig.drafting?.signature || '';

  return {
    to: recipient,
    subject: content.subject || subjectLine(message.subject),
    body: `${content.body || ''}${signature}`.trim()
  };
}
