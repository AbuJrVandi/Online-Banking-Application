import random   # Importing the random module to generate random numbers
import hashlib  # Importing the hashlib module to use hashing functions for security


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

    def hash_pin(self, pin, salt):
        # Method in hashing the PIN using SHA-256 and salt
        return hashlib.sha256((pin + salt).encode()).hexdigest()

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

    def calculate_simple_interest(self, principal, time_years):
        return principal * self.interest_rate * time_years

    def calculate_compound_interest(self, principal, time_years, compounds_per_year=1):
        return principal * (1 + self.interest_rate / compounds_per_year) ** (
                    compounds_per_year * time_years) - principal

    def logout(self):
        # Method to logout the currently logged-in user
        if not self.logged_in_user:
            print("No user is currently logged in.")
            return

        print(f"Logging out {self.logged_in_user}...")
        self.logged_in_user = None
        print("Logout successful.")

def main():
    # Main function to run the banking system
    bank = BankingSystem()   # Create an instance of the BankingSystem(Implementation of the oop concept)

    while True:    # Infinite loop to keep the program running until the user exits
        print("\n--- Online Banking System Sierra Leone ---")
        print("1. Register")
        print("2. Login")
        print("3. Recover PIN")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Transfer")
        print("7. Check Balance")
        print("8. Calculate Deposit Interest")
        print("9. Calculate Compound Interest")
        print("10. Logout")
        print("11. Exit")

        choice = input("Enter your choice (1-11): ")
        
        if choice == '1':
            # Registering a new user
            username = input("Enter username: ")
            pin = input("Enter PIN: ")
            if bank.register_user(username, pin):
                question = input("Set a security question: ")
                answer = input("Set the answer: ")
                bank.set_security_question(question, answer)

        elif choice == '2':
            # User loginig in
            username = input("Enter username: ")
            pin = input("Enter PIN: ")
            bank.login(username, pin)

        elif choice == '3':
            # Recover a forgotten PIN
            username = input("Enter username: ")
            bank.recover_pin(username)

        elif choice == '4':
            # Deposit money into the account
            amount = float(input("Enter deposit amount: "))
            bank.deposit(amount)

        elif choice == '5':
            # Withdraw money from the account
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(amount)

        elif choice == '6':
            # Transfer money to another user
            recipient = input("Enter recipient's username: ")
            amount = float(input("Enter transfer amount: "))
            bank.transfer(recipient, amount)

        elif choice == '7':
            # Check the account balance
            bank.check_balance()

        elif choice == '8':
            # Calculate simple interest on a deposit
            principal = float(input("Enter principal amount: "))
            time = float(input("Enter time in years: "))
            interest = bank.calculate_simple_interest(principal, time)
            print(f"Simple interest: ${interest:.2f}")

        elif choice == '9':
            principal = float(input("Enter principal amount: "))
            time = float(input("Enter time in years: "))
            compounds = int(input("Enter number of times interest is compounded per year: "))
            interest = bank.calculate_compound_interest(principal, time, compounds)
            print(f"Compound interest: ${interest:.2f}")

        elif choice == '10':
            bank.logout()

        elif choice == '11':
            print("Thank you for using our Online Banking System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
        main()