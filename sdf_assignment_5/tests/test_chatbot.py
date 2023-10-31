"""
Description: To verify chatbot.py file  
Author: Dongok Yang
Date: 2023-10-30
Usage: To verify chatbot.py file 
"""
import unittest
from unittest.mock import patch
from src.chatbot import get_account, get_amount, get_balance, make_deposit, user_selection, ACCOUNTS
class ChatbotTests(unittest.TestCase):

    def test_get_account_valid_account(self):
        # Act
        with patch("builtins.input", side_effect=["123456"]):
            
            account = get_account()
            # Assert
            self.assertEqual(account, 123456)

    def test_get_account_non_numeric_account(self):
         
        with patch("builtins.input", side_effect=["non_numeric_data"]):
             # Act
            with self.assertRaises(ValueError) as context:
           
                get_account()
            # Assert
            self.assertEqual(str(context.exception), "Account number must be a whole number.")
    
    def test_get_account_account_does_not_exist(self):
        
        with patch("builtins.input", side_effect=["112233"]):
             # Act 
            with self.assertRaises(Exception) as context:
                get_account()
            # Assert
            self.assertEqual(str(context.exception), "Account number does not exist.")

    def test_get_amount_valid_amount(self):
            # Act
            with patch("builtins.input", side_effect=["500.01"]):
                 
                amount = get_amount()
                # Assert
                self.assertEqual(amount, 500.01)
     
    def test_get_amount_negative(self):
            with patch("builtins.input", side_effect=["0"]):
                # Act
                with self.assertRaises(ValueError) as context:
                    get_amount()
                # Assert
                self.assertEqual(str(context.exception), "Invalid amount. Please enter a positive number.")
    def test89_get_amount_non_numeric(self):               
            with patch("builtins.input", side_effect=["non_numeric_data"]):
                    # Act
                    with self.assertRaises(ValueError) as context:
                        get_amount()
                    # Assert
                    self.assertEqual(str(context.exception), "Invalid amount. Amount must be numeric.")
    def test_get_balance_correct(self):
        # Arrange and Act
        with patch("builtins.input", side_effect=["123456"]): #Mock the user's response to input function
             
            balance_info = get_balance(int(input("Enter an account number: ")))
            expected_output = 'Your current balance for account 123456 is $1,000.00.'
            # Assert
            self.assertEqual(balance_info, expected_output)

    def test_get_balance_account_does_not_exist(self):
        with patch("builtins.input", side_effect=["112233"]): #Mock the user's response to input function
            # Act
            with self.assertRaises(Exception) as context:
                get_balance(int(input("Enter an account number: ")))
            # Assert
            self.assertEqual(str(context.exception), "Account number does not exist.")

    def test_make_deposit_correct_balance(self):
        # Arrange
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0

        # Act
        make_deposit(account_number, 1500.01)

        # Assert
        self.assertEqual(ACCOUNTS[account_number]["balance"], 2500.01)


    def test_make_deposit_correct_output(self):
        # Arrange
        account_number = 123456
        ACCOUNTS[account_number]["balance"] = 1000.0

        # Act
        result = make_deposit(account_number, 1500.01)

        # Assert
        self.assertEqual(result, "You have made a deposit of $1,500.01 to account 123456.")


    def test_make_deposit_account_does_not_exist(self):
        # Arrange
        account_number = 112233
        amount = 1500.01

        # Act and Assert
        with self.assertRaises(Exception) as e:
            make_deposit(account_number, amount)
        
        self.assertEqual(str(e.exception), "Account number does not exist.")


    def test_make_deposit_negative(self):
        # Arrange
        account_number = 123456
        amount = -50.01

        # Act and Assert
        with self.assertRaises(ValueError) as e:
            make_deposit(account_number, amount)
        
        self.assertEqual(str(e.exception), "Invalid amount. Amount must be positive.")

    def test_user_selection_valid_wrong_case(self):
        with patch("builtins.input", return_value="balance"):
            result = user_selection()
            self.assertEqual(result, "balance")

    def test_user_selection_valid_lowercase(self):
        with patch("builtins.input", return_value="DEPOSIT"):
            result = user_selection()
            self.assertEqual(result, "deposit")

    def test_user_selection_invalid(self):
        with patch("builtins.input", return_value="invalid_selection"):
            with self.assertRaises(ValueError) as context:
                user_selection()
            self.assertEqual(str(context.exception), "Invalid task. Please choose balance, deposit, or exit.")

if __name__ == "__main__":
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(ChatbotTests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    unittest.main()



if __name__ == "__main__":
    unittest.main()
