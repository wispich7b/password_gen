import string
import random

def generate_password(length=12):
    """
    Generates a secure random password containing letters, 
    digits, and special characters.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("--- Simple Password Generator ---")
    
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        if length < 4:
            print("Safety warning: Short passwords are easy to crack!")
        
        new_password = generate_password(length)
        print(f"Generated password: {new_password}")
        print("Keep it safe!")
        
    except ValueError:
        print("Error: Please enter a valid number for length.")

if __name__ == "__main__":
    main()
