import random
from onlinebanking_system.hashing import hash_pin
from onlinebanking_system.interest import calculate_simple_interest, calculate_compound_interest


# Defining a class called BankingSystem
class BankingSystem:
    # Constructor method initializes some variables
    def __init__(self):    # Dictionary to store user information(Implementation of data structure)
        self.users = {}
        self.logged_in_user = None
        self.interest_rate = 0.05  # 5% annual interest rate

    def register_user(self, username, pin):
        if username in self.users:
            print("Username already exists. Please choose another.")
            return False
        # Create a salt and hash the PIN
        salt = str(random.randint(1000, 9999))
        hashed_pin = self.hash_pin(pin, salt)
        self.users[username] = {
            'pin': hashed_pin,
            'salt': salt,
            'balance': 0,
            'security_question': None,
            'security_answer': None
        }
        print("Registration successful!")
        return True
    
    def login(self, username, pin):
        # Method to log in a user
        if username not in self.users:
            print("Username not found.")
            return False

        user = self.users[username]
        # Checking if the provided PIN matches the stored hashed PIN
        if self.hash_pin(pin, user['salt']) == user['pin']:
            self.logged_in_user = username
            print("Login successful!")
            return True
        else:
            print("Incorrect PIN.")
            return False

    def set_security_question(self, question, answer):
        if not self.logged_in_user:
            print("Please log in first.")
            return

        self.users[self.logged_in_user]['security_question'] = question
        self.users[self.logged_in_user]['security_answer'] = answer
        print("Security question set successfully.")

    def recover_pin(self, username):
        if username not in self.users:
            print("Username not found.")
            return

        user = self.users[username]
        if not user['security_question']:
            print("No security question set. Unable to recover PIN.")
            return

        print(f"Security Question: {user['security_question']}")
        answer = input("Your answer: ")
        if answer == user['security_answer']:
            new_pin = input("Enter new PIN: ")
            salt = str(random.randint(1000, 9999))
            hashed_pin = self.hash_pin(new_pin, salt)
            user['pin'] = hashed_pin
            user['salt'] = salt
            print("PIN reset successful.")
        else:
            print("Incorrect answer. Unable to reset PIN.")

    def deposit(self, amount):
        # Method to deposit money into user's account
        if not self.logged_in_user:
            print("Please log in first.")
            return

        if amount <= 0:
            print("Invalid amount.")
            return
        
        # Adding the amount to the user's balance
        self.users[self.logged_in_user]['balance'] += amount
        print(f"Deposited ${amount:.2f}")

    # Method to withdraw money from the logged-in user's account
    def withdraw(self, amount):
        if not self.logged_in_user:
            print("Please log in first.")
            return

        if amount <= 0:
            print("Invalid amount.")
            return
        
        # Checking if the user has enough balance
        if self.users[self.logged_in_user]['balance'] < amount:
            print("Insufficient funds.")
            return
        
        # Subtracting the amount from the user's balance
        self.users[self.logged_in_user]['balance'] -= amount
        print(f"Withdrawn ${amount:.2f}")
    
    # Method to transfer money to another user
    def transfer(self, recipient, amount):
        if not self.logged_in_user:
            print("Please log in first.")
            return

        if recipient not in self.users:
            print("Recipient not found.")
            return

        if amount <= 0:
            print("Invalid amount.")
            return

        if self.users[self.logged_in_user]['balance'] < amount:
            print("Insufficient funds.")
            return

        self.users[self.logged_in_user]['balance'] -= amount
        self.users[recipient]['balance'] += amount
        print(f"Transferred ${amount:.2f} to {recipient}")

    def check_balance(self):
        if not self.logged_in_user:
            print("Please log in first.")
            return

        balance = self.users[self.logged_in_user]['balance']
        print(f"Your current balance is ${balance:.2f}")


    def logout(self):
        # Method to logout the currently logged-in user
        if not self.logged_in_user:
            print("No user is currently logged in.")
            return

        print(f"Logging out {self.logged_in_user}...")
        self.logged_in_user = None
        print("Logout successful.")
