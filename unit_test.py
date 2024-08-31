#Import testing Liberies
import unittest
from unittest.mock import patch  
from io import StringIO 
from OnlineBankingApp import BankingSystem

#This is the test-case class
class TestBankingSystem(unittest.TestCase):

    def setUp(self):
        self.bank = BankingSystem()

    #This test function test the user registration
    def test_register_user(self):
        self.assertTrue(self.bank.register_user("team@user", "team@123"))
        self.assertFalse(self.bank.register_user("team@user", "team@123"))

    #This test add a user and then test if the test function can log in with the correct PIN.
    def test_login(self):
        self.bank.register_user("team@user", "team@123")
        self.assertTrue(self.bank.login("team@user", "team@123"))
        self.assertFalse(self.bank.login("team@user", "entered_the_wrong_pin"))
        self.assertFalse(self.bank.login("enter_unknown_user", "team@123"))
    
    #Testing the security question feature
    def test_set_security_question(self):
        self.bank.register_user("team@user", "team@123")
        self.bank.login("team@user", "team@123")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.bank.set_security_question("What is your pet's name?", "Phidel")
            self.assertIn("Security question set successfully.", fake_out.getvalue())
    
    #Unit test that helps us recover a lost PIN using a security question
    @patch('builtins.input', side_effect=["Phidel", "ph@123"])
    def test_recover_pin(self, mock_input):
        self.bank.register_user("team@user", "team@123")
        self.bank.login("team@user", "team@123")
        self.bank.set_security_question("What is your pet's name?", "Phidel")
        self.bank.logout()

        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.bank.recover_pin("team@user")
            self.assertIn("PIN reset successful.", fake_out.getvalue())
    
    #Unit test to test if money can be added
    def test_deposit(self):
        self.bank.register_user("team@user", "team@123")
        self.bank.login("team@user", "team@123")
        self.bank.deposit(100) # Deposit 100
        self.assertEqual(self.bank.users["team@user"]["balance"], 100)
    
    #Unit test to test if money can be withdrawn from account
    def test_withdraw(self):
        self.bank.register_user("team@user", "team@123")
        self.bank.login("team@user", "team@123")
        self.bank.deposit(100)
        self.bank.withdraw(50)
        self.assertEqual(self.bank.users["team@user"]["balance"], 50) #Checking to see if the money(NLE 50) was took out successfully
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.bank.withdraw(100)
            self.assertIn("Insufficient funds.", fake_out.getvalue()) #checking if the function knows when there's not enough money to take out.
    
    #Unit test to test if money can be move from account to another
    def test_transfer(self):
        self.bank.register_user("team@user", "team@123")
        self.bank.register_user("user@team", "user@123")
        self.bank.login("team@user", "team@123")
        self.bank.deposit(100)
        self.bank.transfer("user@team", 50)
        self.assertEqual(self.bank.users["team@user"]["balance"], 50)
        self.assertEqual(self.bank.users["user@team"]["balance"], 50)
    
    #unit-test to test if the function can tell how much money is in the account
    def test_check_balance(self):
        self.bank.register_user("team@user", "team@123")
        self.bank.login("team@user", "team@123")
        self.bank.deposit(100)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.bank.check_balance()
            self.assertIn("Your current balance is $100.00", fake_out.getvalue())
    
    #Unit-test to test if the function can calculate simple interest
    def test_calculate_simple_interest(self):
        self.assertEqual(self.bank.calculate_simple_interest(1000, 2), 100)
    
    #Unit-test to test if the function can calculate compound interest
    def test_calculate_compound_interest(self):
        self.assertAlmostEqual(self.bank.calculate_compound_interest(1000, 2, 1), 102.5, places=2)
    
    #Unit-test to test if a user can log-out successfully
    def test_logout(self):
        self.bank.register_user("team@user", "team@123")
        self.bank.login("team@user", "team@123")
        self.bank.logout()
        self.assertIsNone(self.bank.logged_in_user)

# This runs all the tests when the program is started.
if __name__ == "__main__":
    unittest.main()