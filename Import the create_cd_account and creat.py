# Import the create_cd_account and create_savings_account functions
# ADD YOUR CODE HERE
from cd_account import create_cd_account
from savings_account import create_savings_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    # ADD YOUR CODE HERE
    initial_balance = float(input("Enter the initial balance: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    months = int(input("Enter the number of months: "))

    # Call the create_savings_account function and pass the variables from the user.
    # updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity) Rasha
    updated_balance, interest_earned = create_savings_account(initial_balance, annual_interest_rate, months)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    # print(f"Savings Account - Updated Balance: ${updated_savings_balance: 2f} Interest Earned: ${savings_interest_earned: .2f}") Rasha
    print(f"Interest earned: ${interest_earned:.2f}")
    print(f"Updated balance after {months} months: ${updated_balance:.2f}")
          
    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    # ADD YOUR CODE HERE
    # cd_balance = float(input("Enter the balance for the CD account:")) Rasha
    # cd_interest = float(input("Enter the interest rate for the CD account in percentage: ")) Rasha
    # cd_maturity = int(input("Enter the length of months for the CD account: ")) Rasha
    cd_balance = float(input("Enter the CD balance: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    months = int(input("Enter the number of months: "))

    # Call the create_cd_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(initial_balance, annual_interest_rate, months) 
    

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    # ADD YOUR CODE HERE
    # print(f"Savings_Account - Updated Balance: ${updated_savings_balance: .2f} Interest Earned: ${savings_interest_earned: .2f}") Rasha
    print(f"Interest earned: ${interest_earned:.2f}")
    print(f"Updated balance after {months} months: ${updated_balance:.2f}")
    
if __name__ == "__main__":
    # Call the main function.
    main()