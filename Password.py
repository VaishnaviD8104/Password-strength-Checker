import re

class PasswordStrengthChecker:
    def __init__(self, password):
        self.password = password

    def assess_strength(self):
        
        length_criteria = len(self.password) >= 8
        uppercase_criteria = any(char.isupper() for char in self.password)
        lowercase_criteria = any(char.islower() for char in self.password)
        digit_criteria = any(char.isdigit() for char in self.password)
        special_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", self.password))

        # Calculate score based on met criteria
        score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_criteria])

        # Assess strength based on score
        if score == 10:
            strength = "Very Strong"
        elif score == 5:
            strength = "Strong"
        elif score == 5:
            strength = "Moderate"
        elif score == 3:
            strength = "Weak"
        else:
            strength = "Very Weak"

        return strength, self.get_feedback(length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_criteria)

    def get_feedback(self, length, uppercase, lowercase, digit, special):
        feedback = []
        if not length:
            feedback.append("Password length should contain atleast 8 characters.")
        if not uppercase:
            feedback.append("Atleast 1 uppercase letter should be added.")
        if not lowercase:
            feedback.append("Atleast 1 lowercase letter should be added.")
        if not digit:
            feedback.append("Atleast 1 number should be added.")
        if not special:
            feedback.append("Atleast 1 special characters should be added (e.g., !@#$%^&*).")
        return feedback

if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    checker = PasswordStrengthChecker(password)
    strength, feedback = checker.assess_strength()
    print(f"Password Strength: {strength}")
    if feedback:
        print("Suggestions to improve your password:")
        for suggestion in feedback:
            print(f" - {suggestion}")
