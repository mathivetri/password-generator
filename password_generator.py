import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_lowercase
    elif complexity == 2:
        characters = string.ascii_lowercase + string.ascii_uppercase
    elif complexity == 3:
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    elif complexity == 4:
        characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    else:
        raise ValueError("Invalid complexity level")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("The length must be a positive integer.")
        
        print("Select the complexity level:")
        print("1. Low (lowercase letters)")
        print("2. Medium (lowercase and uppercase letters)")
        print("3. High (lowercase, uppercase letters, and digits)")
        print("4. Very High (lowercase, uppercase letters, digits, and punctuation)")
        complexity = int(input("Enter the complexity level (1-4): "))
        
        if complexity not in [1, 2, 3, 4]:
            raise ValueError("The complexity level must be between 1 and 4.")
        
        password = generate_password(length, complexity)
        print(f"Generated Password: {password}")
    except ValueError as ve:
        print(f"Invalid input: {ve}")

if __name__ == "__main__":
    main()
