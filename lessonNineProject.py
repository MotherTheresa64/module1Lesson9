"""Write a program that prompts the user for two numbers, 
   then divides the first by the second. Handle the exceptions where the 
   user enters invalid data (non-numeric) or tries to divide by zero. """
#First Challenge-------------------------------------------------BELOW

# Define the main function
def main():
    # Prompt the user for two numbers
    try:
        num1 = float(input("Enter the first number please:"))
        num2 = float(input("Enter the second number please:"))
        # Divide the first number by the second
        result = num1 / num2
        # Display the result
        print("The result of dividing", num1, "by", num2, "is", result)
    except ValueError:
        print("You must enter a numeric value")
    except ZeroDivisionError:
        print("You cannot divide by zero")
    except:
        print("An error occurred")
    finally:
        print("Thank you for using my program!")
# Call the main function
main()



"""Create a program that simulates an ATM withdrawal process (Full instructions/requirements listed in README.md)"""
# (FINAL CHALLENGE)---------------------------------------------BELOW

# Define the main function
def main():
    # Initialize the account balance variable
    account_balance = 500
    # Prompt the user for the amount to withdraw
    try:
        amount = float(input("Enter the amount to withdraw:"))
        if amount < 0:
            raise ValueError
        if amount > account_balance:
            raise Exception
        account_balance -= amount
        print("The remaining balance is", account_balance)
    except ValueError:
        print("You must enter a positive numeric value")
    except Exception:
        print("Insufficient funds")
    except:
        print("An error occurred")
    finally:
        print("Thank you for using my program!")
# Call the main function
main()
