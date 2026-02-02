def detect_intent(text: str) -> str:
    text = text.lower()

    if "emi" in text or "loan" in text:
        return "LOAN"
    if "transaction" in text or "debit" in text or "credit" in text:
        return "TRANSACTION"
    if "balance" in text:
        return "BALANCE"

    return "GENERAL"
