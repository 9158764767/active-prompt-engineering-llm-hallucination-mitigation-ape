"""
prompts.py  –  Exact prompt templates from Appendix A of the paper
===================================================================
Every string here is EXACTLY what gets sent to the model.
These are the prompts quoted in the paper — no variations.
"""

DOMAIN_PERSONAS = {
    "general":    "a knowledgeable expert in general knowledge, science, history, and world facts",
    "finance":    "a Chartered Financial Analyst (CFA) with deep expertise in financial markets, "
                  "accounting, economics, and regulatory frameworks",
    "healthcare": "a licensed medical doctor (MD) with expertise in clinical medicine, "
                  "pharmacology, and evidence-based practice",
    "legal":      "a senior licensed attorney with expertise in constitutional law, "
                  "federal law, and international legal frameworks",
}

STRATEGIES = ["baseline", "constraint", "cot", "cove", "ape"]

STRATEGY_LABELS = {
    "baseline":   "Baseline",
    "constraint": "Constraint (C)",
    "cot":        "Chain-of-Thought (R)",
    "cove":       "Chain-of-Verification (V)",
    "ape":        "APE (C+R+V)",
}


def build_prompt(query: str, strategy: str, domain: str = "general") -> list[dict]:
    """
    Returns a list of message dicts (role, content) for the given strategy.
    This is EXACTLY what is passed to the model API.
    Strings match Appendix A of the paper verbatim.
    """
    persona = DOMAIN_PERSONAS.get(domain, DOMAIN_PERSONAS["general"])

    if strategy == "baseline":
        # ── Appendix A: Baseline ─────────────────────────────────────────
        return [{"role": "user", "content": query}]

    elif strategy == "constraint":
        # ── Appendix A: Constraint Prompt (C) ────────────────────────────
        text = (
            f"You are {persona}.\n\n"
            "Answer the following question only if you are highly confident in your response. "
            "If you are uncertain or do not know the answer, respond with \"I don't know\" "
            "rather than estimating. Do not speculate.\n\n"
            f"Question: {query}"
        )
        return [{"role": "user", "content": text}]

    elif strategy == "cot":
        # ── Appendix A: Chain-of-Thought Prompt (R) ──────────────────────
        text = (
            f"You are {persona}.\n\n"
            "Think step by step to answer the following question. "
            "Show your reasoning before providing the final answer.\n\n"
            f"Question: {query}"
        )
        return [{"role": "user", "content": text}]

    elif strategy == "cove":
        # ── Appendix A: Chain-of-Verification Prompt (V) ─────────────────
        text = (
            f"You are {persona}.\n\n"
            "Follow these four steps:\n"
            "1. Answer the question.\n"
            "2. Generate verification questions to check your answer.\n"
            "3. Answer those verification questions.\n"
            "4. If inconsistencies are found, revise your answer. "
            "Provide only the final, revised answer.\n\n"
            f"Question: {query}"
        )
        return [{"role": "user", "content": text}]

    elif strategy == "ape":
        # ── Appendix A: APE Prompt (C+R+V) ───────────────────────────────
        text = (
            f"You are {persona}. Follow these instructions:\n\n"
            "[CONSTRAINTS] Only respond if you are highly confident. "
            "If uncertain, state \"I don't know.\" Do not speculate. "
            "Stay within the factual domain of the question.\n\n"
            "[REASONING] Think step by step: "
            "(1) What is being asked? "
            "(2) What are the relevant facts? "
            "(3) What is the logical conclusion?\n\n"
            "[VERIFICATION] Before finalizing: "
            "(a) Are all claims supported? "
            "(b) Are there contradictions? "
            "(c) Is there a more accurate response? "
            "Revise if necessary.\n\n"
            f"Question: {query}"
        )
        return [{"role": "user", "content": text}]

    else:
        raise ValueError(f"Unknown strategy: {strategy!r}. Choose from {STRATEGIES}")
