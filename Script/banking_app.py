from onlinebanking_system.banking import BankingSystem
from onlinebanking_system.interest import BankingSystem

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