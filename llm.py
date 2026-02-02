import random

# ---------------- Knowledge Base ---------------- #

FINANCE_KB = {
    "EMI": {
        "keywords": ["emi", "installment", "monthly payment"],
        "response": [
            "EMI (Equated Monthly Installment) is a fixed monthly amount "
            "paid by a borrower to repay a loan. It includes both principal "
            "and interest.",

            "An EMI allows you to repay large loans in manageable monthly "
            "payments instead of paying the full amount at once."
        ],
        "follow_up": "Do you want to know how EMI is calculated?"
    },

    "INTEREST": {
        "keywords": ["interest", "rate", "percentage"],
        "response": [
            "Interest is the extra money charged by a bank for lending funds. "
            "It is usually calculated as a percentage of the loan amount.",

            "Higher interest rates increase your EMI, while lower rates "
            "reduce your repayment burden."
        ],
        "follow_up": "Would you like an example with numbers?"
    },

    "TRANSACTION": {
        "keywords": ["transaction", "debit", "credit", "payment"],
        "response": [
            "A transaction is any movement of money into or out of your "
            "bank account, such as UPI payments, ATM withdrawals, or deposits.",

            "Each debit or credit entry in your bank statement is "
            "called a transaction."
        ],
        "follow_up": "Do you want help understanding a specific transaction?"
    },

    "BALANCE": {
        "keywords": ["balance", "amount left", "money left"],
        "response": [
            "Your account balance is the amount of money currently "
            "available in your bank account.",

            "You can check your balance using mobile banking, ATMs, "
            "or bank statements."
        ],
        "follow_up": "Would you like tips to manage your balance better?"
    }
}

# ---------------- Core LLM Logic ---------------- #

def score_match(text, keywords):
    """Returns how strongly user text matches a topic"""
    score = 0
    for word in keywords:
        if word in text:
            score += 1
    return score


def get_llm_response(context, intent):
    """
    Advanced offline LLM-style response generator.
    Uses semantic scoring + context awareness.
    """

    user_text = context[-1]["content"].lower()

    best_topic = None
    best_score = 0

    # Semantic scoring
    for topic, data in FINANCE_KB.items():
        score = score_match(user_text, data["keywords"])
        if score > best_score:
            best_score = score
            best_topic = topic

    # If strong match found
    if best_topic:
        response = random.choice(FINANCE_KB[best_topic]["response"])
        follow_up = FINANCE_KB[best_topic]["follow_up"]
        return f"{response} {follow_up}"

    # Intent-based fallback
    if intent == "LOAN":
        return (
            "Loans help you borrow money for needs like education, housing, "
            "or business, which you repay over time with interest. "
            "Would you like details on EMI or interest?"
        )

    # Final fallback
    return (
        "I specialize in banking and financial topics such as EMI, loans, "
        "interest rates, transactions, and account balance. "
        "Please ask a finance-related question."
    )