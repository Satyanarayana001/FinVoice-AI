# prompts.py
# Centralized, clean, human-friendly finance responses

PROMPTS = {

    "EMI_DEFINITION": {
        "short": (
            "EMI stands for Equated Monthly Installment. "
            "It is the fixed amount you pay every month to repay a loan."
        ),
        "detailed": (
            "EMI stands for Equated Monthly Installment. "
            "It is the fixed amount paid every month to repay a loan, "
            "including both the principal amount and the interest. "
            "The EMI amount usually remains constant throughout the loan tenure."
        )
    },

    "EMI_CALCULATION": {
        "short": (
            "EMI is calculated using the loan amount, interest rate, and tenure."
        ),
        "detailed": (
            "EMI is calculated based on three factors: "
            "the loan amount, the interest rate, and the loan tenure. "
            "A higher loan amount or interest rate increases the EMI, "
            "while a longer tenure reduces the monthly EMI but increases total interest paid."
        )
    },

    "LOAN_INTEREST": {
        "short": (
            "Loan interest is the extra amount paid to the lender for borrowing money."
        ),
        "detailed": (
            "Loan interest is the cost charged by a lender for providing a loan. "
            "It is usually expressed as a percentage and can be fixed or floating. "
            "Interest is added to the principal and repaid through EMIs."
        )
    },

    "BANKING_BASICS": {
        "short": (
            "Banking transactions include deposits, withdrawals, and transfers."
        ),
        "detailed": (
            "Banking transactions include deposits, withdrawals, transfers, "
            "and digital payments. These transactions help individuals manage "
            "their money securely through bank accounts."
        )
    },

    "DEBIT_CREDIT": {
        "short": (
            "Debit means money going out, credit means money coming in."
        ),
        "detailed": (
            "Debit refers to money being taken out of your bank account, "
            "such as when you make a payment. Credit refers to money added "
            "to your account, such as salary or deposits."
        )
    },

    "UNKNOWN": {
        "short": (
            "I’m not sure about that. Please ask a finance-related question."
        ),
        "detailed": (
            "I’m sorry, I don’t have information on that topic yet. "
            "Please ask a basic finance-related question like EMI, loans, or banking."
        )
    }
}