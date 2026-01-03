def evaluate_claim(claim):
    if not claim["policy_active"]:
        return "Rejected: Policy is inactive."

    if claim["amount"] > 500000:
        return "Needs Review: Claim amount exceeds standard limit."

    if not claim["documents_submitted"]:
        return "Needs Review: Required documents missing."

    return "Approved: Claim meets all basic criteria."
