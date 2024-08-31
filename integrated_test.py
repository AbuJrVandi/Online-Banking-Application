#Import testing Liberies
import unittest
from unittest.mock import patch  
from io import StringIO 
from OnlineBankingApp import BankingSystem

#This is the test-case class
class TestBankingSystem(unittest.TestCase):

    def setUp(self):
        self.bank = BankingSystem()
        
def test_integration_workflow(self):
    self.bank.register_user("team@user", "team@123")
    self.bank.register_user("user@team", "5678")
    self.bank.login("team@user", "team@123")
    self.bank.deposit(100)
    self.bank.transfer("user@team", 50)
    self.assertEqual(self.bank.users["team@user"]["balance"], 50)
    self.assertEqual(self.bank.users["team@user"]["balance"], 50)