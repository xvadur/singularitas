const CATEGORY_RULES = {
  newsletter: ['newsletter', 'unsubscribe', 'substack', 'digest', 'weekly update'],
  finance: ['invoice', 'payment', 'paid', 'bank', 'wire', 'tax', 'receipt', 'billing'],
  legal: ['contract', 'agreement', 'nda', 'lawyer', 'legal', 'terms', 'privacy'],
  lead: ['quote', 'proposal', 'interested', 'pricing', 'project', 'book a call', 'partnership'],
  provider: ['hosting', 'vendor', 'supplier', 'service update', 'maintenance', 'account manager'],
  ignore: ['no-reply', 'noreply', 'notification', 'automated message']
};

function heuristicClassify(message, allowedCategories) {
  const haystack = `${message.subject}\n${message.from}\n${message.snippet}\n${message.bodyText}`.toLowerCase();

  for (const category of allowedCategories) {
    const keywords = CATEGORY_RULES[category] || [];
    if (keywords.some((keyword) => haystack.includes(keyword))) {
      return {
        category,
        confidence: 0.55,
        reasoning: `Heuristic match on keywords for '${category}'.`
      };
    }
  }

  return {
    category: 'other',
    confidence: 0.35,
    reasoning: 'No heuristic rule matched strongly.'
  };
}

async function classifyWithOpenAiCompatible({ aiConfig, message, allowedCategories }) {
  const apiKey = process.env[aiConfig.apiKeyEnv];
  if (!apiKey) {
    throw new Error(`Missing AI API key in env ${aiConfig.apiKeyEnv}.`);
  }

  const prompt = {
    categories: allowedCategories,
    instructions: [
      'Classify the email into exactly one category.',
      'Decide whether it likely needs a human reply.',
      'Decide whether drafting a reply would be helpful.',
      'Keep reasoning short and practical.',
      'Never suggest sending automatically.'
    ],
    email: {
      from: message.from,
      subject: message.subject,
      snippet: message.snippet,
      bodyText: message.bodyText.slice(0, 4000)
    },
    responseSchema: {
      category: 'one of the provided categories',
      confidence: 'number between 0 and 1',
      needsReply: 'boolean',
      shouldDraftReply: 'boolean',
      reasoning: 'short string',
      draftReplyInstructions: 'short string or empty'
    }
  };

  const response = await fetch(`${aiConfig.baseUrl}/chat/completions`, {
    method: 'POST',
    headers: {
      'content-type': 'application/json',
      authorization: `Bearer ${apiKey}`
    },
    body: JSON.stringify({
      model: aiConfig.model,
      temperature: 0.1,
      response_format: { type: 'json_object' },
      messages: [
        {
          role: 'system',
          content: 'You classify business email for a local mail triage worker. Output JSON only.'
        },
        {
          role: 'user',
          content: JSON.stringify(prompt)
        }
      ]
    })
  });

  if (!response.ok) {
    const body = await response.text();
    throw new Error(`AI request failed (${response.status}): ${body}`);
  }

  const payload = await response.json();
  const content = payload?.choices?.[0]?.message?.content;
  const parsed = JSON.parse(content);

  if (!allowedCategories.includes(parsed.category)) {
    throw new Error(`AI returned unsupported category '${parsed.category}'.`);
  }

  return parsed;
}

export async function classifyMessage({ aiConfig, mailboxConfig, message }) {
  const allowedCategories = mailboxConfig.classification.categories;
  const heuristic = heuristicClassify(message, allowedCategories);

  if (!mailboxConfig.classification.preferAi) {
    return {
      ...heuristic,
      needsReply: ['lead', 'finance', 'legal', 'provider'].includes(heuristic.category),
      shouldDraftReply: ['lead', 'finance', 'legal'].includes(heuristic.category),
      draftReplyInstructions: ''
    };
  }

  try {
    const aiResult = await classifyWithOpenAiCompatible({ aiConfig, message, allowedCategories });
    return {
      ...heuristic,
      ...aiResult,
      reasoning: aiResult.reasoning || heuristic.reasoning
    };
  } catch (error) {
    return {
      ...heuristic,
      needsReply: ['lead', 'finance', 'legal', 'provider'].includes(heuristic.category),
      shouldDraftReply: mailboxConfig.classification.draftReplyCategories.includes(heuristic.category),
      draftReplyInstructions: '',
      aiError: error.message
    };
  }
}
