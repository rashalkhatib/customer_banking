Customer Banking System
# Savings and CD Account Interest Calculator

This system calculates the interest earned on savings and CD accounts based on user input for initial balance, interest rate, and the number of months. It uses the `create_cd_account` and `create_savings_account` to perform the calculations.

## Code Structure

### Importing Functions
- The system imports the `create_cd_account` and `create_savings_account` functions from (`cd_account.py` and `savings_account.py`).

### Main Function
- The `main` function is defined to handle the main logic of the script.
- It prompts the user to input the savings account balance, interest rate, and months.
- The `create_savings_account` function calculates the interest earned and updates the savings account balance.
- It asks the user to enter the CD account balance, interest rate, and months.
- The `create_cd_account` function to calculates the interest earned and updates the CD account balance.

## How to Use

2. **Set Savings Account Parameters**
   - Ask the user to input the initial savings account balance, annual interest rate (in percentage), and the number of months.

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



