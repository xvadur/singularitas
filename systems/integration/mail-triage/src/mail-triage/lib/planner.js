function cleanLabels(labels = []) {
  return [...new Set(labels.filter(Boolean))];
}

export function buildActionPlan({ mailboxConfig, message, classification }) {
  const categoryLabel = mailboxConfig.labels.categories[classification.category];
  const addLabels = [mailboxConfig.labels.processed, categoryLabel];
  const removeLabels = [];

  if (classification.needsReply) {
    addLabels.push(mailboxConfig.labels.needsReply, mailboxConfig.labels.awaitingHuman);
  }

  if (classification.category === 'newsletter' || classification.category === 'ignore') {
    removeLabels.push('UNREAD');
  }

  const confidentEnoughForDraft = Number(classification.confidence || 0) >= 0.75;

  return {
    category: classification.category,
    addLabels: cleanLabels(addLabels),
    removeLabels: cleanLabels(removeLabels),
    shouldDraftReply:
      Boolean(mailboxConfig.drafting?.enabled) &&
      Boolean(classification.needsReply) &&
      Boolean(classification.shouldDraftReply) &&
      confidentEnoughForDraft &&
      mailboxConfig.classification.draftReplyCategories.includes(classification.category),
    needsReply: Boolean(classification.needsReply)
  };
}
