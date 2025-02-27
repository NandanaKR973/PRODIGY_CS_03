import re

def assess_password_strength(password):
    
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'[0-9]', password) is not None
    special_char_criteria = re.search(r'[@$!%*?&]', password) is not None

   
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    
    if criteria_met == 5:
        strength = "Very Strong"
        feedback = "Your password is very strong! It meets all criteria."
    elif criteria_met == 4:
        strength = "Strong"
        feedback = "Your password is strong! It meets most criteria."
    elif criteria_met == 3:
        strength = "Moderate"
        feedback = "Your password is moderate. Consider adding more complexity."
    elif criteria_met == 2:
        strength = "Weak"
        feedback = "Your password is weak. Please improve it by adding more variety."
    else:
        strength = "Very Weak"
        feedback = "Your password is very weak. It does not meet the minimum requirements."

    return strength, feedback

if __name__ == "__main__":
    password = input("Enter a password to assess its strength: ")
    strength, feedback = assess_password_strength(password)
    print(f"Password Strength: {strength}")
    print(feedback)
