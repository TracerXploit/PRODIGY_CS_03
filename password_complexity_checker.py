import re

def complexity_checker(password):
    strength=0
    feedback=[]
    
    # Length check
    if len(password)>=8:
        strength+=1
    else:
        feedback.append("Password should be at least 8 characters long.")    
        
    # Uppercase and lowercase letters check  
    if  re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        strength+=1
    else:
        feedback.append("Password should contain both uppercase and lowercase letters.")
        
    # Number check
    if re.search(r'\d', password):
        strength+=1
    else:
        feedback.append("Password should contain numbers.")
        
    # Special characters check
    if re.search(r'[@$!%*?&#]', password):
        strength+=1
    else:
        feedback.append("Password should contain special characters like @$!%*?&#.")
        
    return strength, "\n".join(feedback)

def strength_of_password(strength):
    feedback=[]
    
 # Password strength evaluation
    if strength == 4:
        feedback.append("Password is very strong.")
    elif strength == 3:
        feedback.append("Password is strong.")
    elif strength == 2:
        feedback.append("Password is medium.")
    else:
        feedback.append("Password is weak.")

    return "\n".join(feedback)
 
def main():
    password = input("Enter a password to check its strength: ")
    strength, complexity_feedback = complexity_checker(password)
    print("\nFeedback: ")
    print(complexity_feedback)
    print("\nStrength Evaluation: ")
    print(strength_of_password(strength))
    
if __name__ == "__main__":
    main()