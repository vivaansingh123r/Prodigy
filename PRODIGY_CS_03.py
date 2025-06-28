import re

def check_password_strength(password):
    score = 0
    feedback = []

    # Criteria checks
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character (e.g., !, @, #, etc.).")

    # Strength result
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    # Output
    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions:")
        for f in feedback:
            print(f" - {f}")

# Example usage
if __name__ == "__main__":
    user_password = input("Enter your password: ")
    check_password_strength(user_password)
