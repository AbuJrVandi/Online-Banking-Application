import unittest
from onlinebanking_system.banking import BankingSystem

class TestBankingSystemIntegration(unittest.TestCase):

    def setUp(self):
        self.bank = BankingSystem()

    def test_register_and_login(self):
        # Register a new user
        self.bank.register_user("integration_user", "integration_pin")
        # Login with the newly registered user
        login_result = self.bank.login("integration_user", "integration_pin")
        self.assertTrue(login_result)

    def test_deposit_and_check_balance(self):
        # Register and login a user
        self.bank.register_user("integration_user", "integration_pin")
        self.bank.login("integration_user", "integration_pin")

        # Deposit money and check balance
        self.bank.deposit(500)
        balance = self.bank.users["integration_user"]["balance"]
        self.assertEqual(balance, 500)

    def test_withdraw_and_transfer(self):
        # Register and login users
        self.bank.register_user("user1", "pin1")
        self.bank.register_user("user2", "pin2")
        self.bank.login("user1", "pin1")

        # Deposit and then withdraw money
        self.bank.deposit(300)
        self.bank.withdraw(100)
        self.assertEqual(self.bank.users["user1"]["balance"], 200)

        # Transfer money to another user
        self.bank.transfer("user2", 100)
        self.assertEqual(self.bank.users["user1"]["balance"], 100)
        self.assertEqual(self.bank.users["user2"]["balance"], 100)

    def test_interest_calculation(self):
        # Register and login a user
        self.bank.register_user("integration_user", "integration_pin")
        self.bank.login("integration_user", "integration_pin")

        # Deposit money
        self.bank.deposit(1000)
        
        # Calculate and verify simple interest
        simple_interest = self.bank.calculate_simple_interest(1000, 2)
        self.assertEqual(simple_interest, 100)

        # Calculate and verify compound interest
        compound_interest = self.bank.calculate_compound_interest(1000, 2, 1)
        self.assertAlmostEqual(compound_interest, 102.5, places=2)

if __name__ == "__main__":
    unittest.main()
