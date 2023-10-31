"""
Description: Chatbot application.  Allows user to perform 
balance inquiries and make deposits to their accounts.
Author: ACE Department
Modified by: Dongok Yang
Date: 2023-10-15
Usage: From the console: python src/chatbot.py
"""

## GIVEN CONSTANT COLLECTIONS
ACCOUNTS = {
    123456 : {"balance" : 1000.0},
    789012 : {"balance" : 2000.0}
}

VALID_TASKS = {"balance", "deposit", "exit"}

## CODE REQUIRED FUNCTIONS STARTING HERE:

def get_account()->int:
    """
    get_account function prompt user for an account number 
    it verifies input is a valid number.

Returns:
    int: The valid account number entered by the user.
Raises:
    ValueError: If the user enters an account number that is not a whole number.
    Exception: If the entered account number does not exist in the ACCOUNTS dictionary.
"""
    account_input = input("Please enter your account number:")
    try : 
        account_number = int(account_input)
        if account_number not in ACCOUNTS:
            raise Exception("Account number entered does not exist.")
        return account_number
    except:
        print("Account number must be a whole number.")
    
def get_amount()->float:
    """
    get_amount function prompt user for an amount.
    It verifies input is a valid number.

Returns:
    float: The valid amount number entered by the user.
Raises:
    ValueError: If the user enters an amount that is not numeric.
    Exception: If the entered amount below or equal to zero.
"""
    amount_input = input("Please enter your account number:")
    try : 
        amount_input = float(amount_input)
        if amount_input <= 0:
            raise Exception("Invalid amount. Please enter a positive number.")
    except:
        print("Invalid amount. Amount must be numeric.")
    return amount_input

def get_balance(account: int)->str:
    """
    get_balance function receive an integer parameter.
    it returns balance information.

args:
    account(int) : the account number that blance is requested.
Returns:
    str: a message representing the balance for account.
Raises:
    Exception: If the account isn't in the Account library.
"""
    if account in ACCOUNTS:
        balance = ACCOUNTS[account]["balance"]
        return f'Your current balance for account {account} is ${balance:,.2f}.'
    else:
        raise Exception('Account number does not exist.')    

def make_deposit(account: int,amount:float)->str:
    """
    make_deposit function receive two parameters.
    it makes a deposit.

args:
    account(int) : the account number that deposit is requested.
    amount(float) : the amount of money to be deposited.
Returns:
    str: a confirmation message.
Raises:
    Exception: If the account isn't in the Account dictionary.
    ValueError: If the provided amount of money is not proper.
"""
    if account not in ACCOUNTS:
        raise Exception("Account number does not exist.")

    if amount <= 0:
        raise ValueError("Invalid amount. Amount must be positive.")

    ACCOUNTS[account]["balance"] += amount
    return f"You have made a deposit of ${amount:,.2f} to account {account}."




## GIVEN CHATBOT FUNCTION
## REQUIRES REVISION
"""
def chatbot():
    '''
    The main program.  Uses the functionality of the functions:
        get_account()
        get_amount()
        get_balance()
        make_deposit()
        user_selection()
    '''

    print("Welcome! I'm the PiXELL River Financial Chatbot!  Let's get chatting!")

    keep_going = True
    while keep_going:
        try:
            ## CALL THE user_selection FUNCTION HERE 
            ## CAPTURING THE RESULTS IN A VARIABLE CALLED
            ## selection:


            if selection != "exit":
                
                # Account number validation.
                valid_account = False
                while valid_account == False:
                    try:
                        ## CALL THE get_account FUNCTION HERE
                        ## CAPTURING THE RESULTS IN A VARIABLE 
                        ## CALLED account:


                        valid_account = True
                    except Exception as e:
                        # Invalid account.
                        print(e)
                if selection == "balance":
                        ## CALL THE get_balance FUNCTION HERE
                        ## PASSING THE account VARIABLE DEFINED 
                        ## ABOVE, AND PRINT THE RESULTS:

                else:

                    # Amount validation.
                    valid_amount = False
                    while valid_amount == False:
                        try:
                            ## CALL THE get_amount FUNCTION HERE
                            ## AND CAPTURE THE RESULTS IN A VARIABLE 
                            ## CALLED amount:


                            valid_amount = True
                        except Exception as e:
                            # Invalid amount.
                            print(e)
                    ## CALL THE make_deposit FUNCTION HERE PASSING THE 
                    ## VARIABLES account AND amount DEFINED ABOVE AND 
                    ## PRINT THE RESULTS:


            else:
                # User selected 'exit'
                keep_going = False
        except Exception as e:
            # Invalid selection:
            print(e)

    print("Thank you for banking with PiXELL River Financial.")
"""
    
"""
if __name__ == "__main__":
    chatbot()
"""