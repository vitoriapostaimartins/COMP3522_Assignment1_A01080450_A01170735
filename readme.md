# Assignment 1 : The F.A.M.

### Prerequisites: Install Tabulate
- Please install the `tabulate` module library before running the program
    - this library is for formatting our outputs into tables
```python
pip install tabulate
```

## How it works
Start the program by running the `driver.py` module

#### Registration and Login
On startup, you will be prompted to enter user details. This includes
the type of User (Angel, Rebel, or Troublemaker) that the child is. 
Then you will be asked to enter the Budget limits for each category (Games and Entertainment, Clothing and Accessories
Eating Out, and Miscellaneous).

After entering the details of the user and their bank account, the new user is created and added to the user list. 
You will then be able to logout and log back in from the main menu if you choose to.

#### Actions (User) Menu
After successfully logging in or registering, a menu is displayed with the following actions:

1. **View Budgets**
   - Shows the current status of your budget (locked or not), amount spent, amount left, the budget balance via console message
2. **Record Transaction**
   - Prompts you to enter transaction details for dollar amount, budget category, name of the shop/website. Then, saves the transaction with the time of the purchase
3. **View Transactions by Budget**
   - Displays budget categories as options, and prompts the user to choose a budget. Then, prints the transactions for the chosen budget.
4. **View Bank Account Details**
   - Prints out the bank account details of the user, all transactions conducted, and the closing balance
5. **Logout**
    - Returns you to the main menu
After completing any of these actions, you will be taken back to this Actions menu.
      

## Features
### Requirements as outlined in the assignment:
- Different User Types
- Recording transactions to different Budgets
- Locking out specific users from their budgets
- Locking out the Rebel from their account
- Notifications and warnings displayed after specific percentage of budget limit spent

### Error Handling
- handles:
    - string inputs in menus that prompt a user for a number
    - using the FAM system when the user is locked out of their accounts
    - negative or zero values for transaction amount
    - transaction amounts that would result in a negative bank balance
    - negative or 0 bank/budget balances
    - making a transaction related to a locked budget
    - making a transaction that has a negative or zero amount.
    
#### Custom Exceptions:
- **UserIsLockedError**
  - Exception for when the user is locked out of their accounts.
- **InvalidBalanceError**
  - Exception for when the user tries to input a value that would result in a negative or zero bank/budget balance.
- **BudgetIsLockedError**
  - Exception for when the user tries to make a transaction in a budget that is locked.
- **TransactionAmountError**
  - Exception for when the user enters an invalid transaction amount, such as negative values or zero.