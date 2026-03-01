import re

PHISHING_PATTERNS = [
    r"verify your account",
    r"urgent action required",
    r"click here",
    r"reset your password",
    r"login immediately",
    r"confirm your identity"
]

def check_text(text: str):
    patterns = [
        "click here",
        "verify your account",
        "urgent",
        "reset password",
        "confirm identity"
    ]

    matched = [p for p in patterns if p in text.lower()]

    risk = "LOW"
    if len(matched) >= 2:
        risk = "HIGH"
    elif len(matched) == 1:
        risk = "MEDIUM"

    return {
        "is_phishing": len(matched) > 0,
        "risk_level": risk,
        "matched_patterns": matched
    }