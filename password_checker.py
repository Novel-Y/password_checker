#!/usr/bin/env python3

"""
This script checks if a user-entered password meets the minimum length requirement of 4 characters.

It repeatedly prompts the user for input until a valid password is provided.

Example Usage:
    python password_checker.py 
"""

def check_password():
    """
    Checks if the entered password meets the minimum length requirement.

    Returns:
        None: If the password is too short.
        str: The valid password if it meets the length requirement.
    """
    
    while True:
        password = input("Enter your password: ")
        password = password.lower()
        assert isinstance(password, str)
   
        if len(password) >= 4:
            print("Password registered")
            return password
        else:
            print("Password too short. Must be at least 4 characters.")

if __name__ == "__main__":
    registered_password = check_password() 
    if registered_password:
        print(f"Registered Password: {registered_password}")