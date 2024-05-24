Customer Banking System
# Savings and CD Account Interest Calculator

This system calculates the interest earned on savings and CD (Certificate of Deposit) accounts based on user input for initial balance, interest rate, and the number of months. It uses the `create_cd_account` and `create_savings_account` functions to perform the calculations.

## Usage

1. Follow the prompts to enter the initial balance, annual interest rate, and months for the savings and CD accounts.

2. The system calculates the interest earned and updates both account balances.

## Code Structure

### Importing Functions
- The script imports the `create_cd_account` and `create_savings_account` functions from their respective modules (`cd_account.py` and `savings_account.py`).

### Main Function
- The `main` function is defined to handle the main logic of the script.
- It prompts the user to input the savings account balance, interest rate, and months.
- It calls the `create_savings_account` function to calculate interest earned and update the savings account balance.
- It then prompts the user to input the CD account balance, interest rate, and months.
- It calls the `create_cd_account` function to calculate interest earned and update the CD account balance.

## How to Use

1. **Import Functions**
   - Import the `create_cd_account` and `create_savings_account` functions from their respective modules.

2. **Set Savings Account Parameters**
   - Prompt the user to input the initial savings account balance, annual interest rate (in percentage), and the number of months.

3. **Calculate Savings Account Interest**
   - Call the `create_savings_account` function with the user-provided parameters.
   - Display the interest earned and the updated savings account balance after the specified months.

4. **Set CD Account Parameters**
   - Prompt the user to input the initial CD account balance, annual interest rate (in percentage), and the number of months.

5. **Calculate CD Account Interest**
   - Call the `create_cd_account` function with the user-provided parameters.
   - Display the interest earned and the updated CD account balance after the specified months.

## Summary

This system allows the user to calculate the interest earned on both savings and CD accounts. It considers the initial balance, annual interest rate, and the duration in months and provides the interest calculations and updated balances for both accounts.



