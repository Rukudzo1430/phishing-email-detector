def check_email(email_text):
    suspicious_phrases = [
        "verify your account",
        "urgent action required",
        "click here",
        "password",
        "account suspended",
        "claim your prize"
    ]

    score = 0
    warnings = []
    text = email_text.lower()

    for phrase in suspicious_phrases:
        if phrase in text:
            score += 1
            warnings.append(f"Suspicious phrase: {phrase}")

    if "http://" in text or "https://" in text:
        score += 1
        warnings.append("Email contains a link")

    print("\n===== EMAIL ANALYSIS =====")

    if score >= 3:
        print("Risk Level: HIGH")
    elif score >= 1:
        print("Risk Level: MEDIUM")
    else:
        print("Risk Level: LOW")

    print("Risk Score:", score)

    if warnings:
        print("\nWarning signs:")
        for warning in warnings:
            print("-", warning)
    else:
        print("No obvious warning signs detected.")

    print("\nThis result is only an initial screening.")


def main():
    print("PHISHING EMAIL DETECTOR")
    print("1. Analyse an email")
    print("2. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        email = input("Paste sample email text: ")
        check_email(email)
    elif choice == "2":
        print("Goodbye!")
    else:
        print("Invalid choice. Please run the program again.")


if __name__ == "__main__":
    main()