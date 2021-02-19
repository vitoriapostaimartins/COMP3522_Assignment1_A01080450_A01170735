Current Progress
================
- [x] **Show user menu**
  - View Budgets, Record Transaction, View Transactions by Budget, View Bank Account Details
- [x] **Recording Transactions**
  - [x] Record & display transactions for a Budget
  - [x] Update Bank Account balance with each transaction
  - [x] User cant record transaction that will cause balance to fall below 0
- [x] **User Registration**
  - register different User Types
- [x] **Main Menu**
  - display on startup
  ```python
    1 - Register new user
    2 - Login
    3 - Exit
  ```
- [x] **User Login**
  - store registered users in list, allow login functionality
- [x] **Login Menu**
  - display if login chosen from main menu
  ```python
    1 - Jeff (Rebel)
    2 - Mike (Troublemaker)
    3 - Shachi (Angel)
    4 - Back to main menu
  ```
- [x] **Notifications**
  - [x] Enum to store message types
  - [x] Perform check after transaction to see if warning or notification should be issued
    - [x] Notify if exceed budget category TEST
         - polite or rude message
    - [x] Warning if exceed a % of budget TEST
      - Angel: >90%
      - Troublemaker: >70%
      - Rebel: >50%
    - [x] Print list of transactions
        - After warning that they are close to exceeding budget for a category
        - After notification that they have exceeded budget for a category
  
- [x] **Lockout - Budget**
  - for Troublemaker and Rebel
  - [x] Lock out from recording transactions (i.e. spending money)
    - Troublemaker: if exceed >120%
    - Rebel: if exceed >100%
  - [x] Notify via console message
  - [x] Deny attempts at recording transactions in affected budget
  
- [x] **Lockout - Account (Rebel)**
    - exceed budget in 2+ categories = lock out from account
  
**TEST**
- [x] handle string inputs for when we ask user for input
- [x] handle negative values for when user tries to spend money
- [x] test notifications
  - if exceed budget category
      - Troublemaker: >120%
      - Rebel: >100%
- [x] test warning
  - if exceed % percentage
      - Angel: >90%
      - Troublemaker: >70%
      - Rebel: >50%
- [x] test lockouts
  - Angel doesn't get locked out of budget or account
  - Troublemaker gets locked out of budget but not account
  - Rebel gets locked out of budget and account
- clean up methods
  - [x] record_transaction
  - [x] on_complete
  - [x] method visibilities are consistent
  - [x] getter/setter -> make consistent
  - [x] user-type specific attributes (k)
  
- ascii art
  - clean up notifications, bank details, transactions etc.
  - ascii tables
- UML diagram cleanup
  - fix arrows
- move to new repo
- make a proper readme file
- add comments
- driver.py module

**Grading**
- [ ] Implement all requirements `10 marks`
- [ ] Correctly format and comment code `2 marks`
  - Eliminate warnings offered by PyCharm
  - good function & variable names, docstrings
- [ ] Structure/design classes to maximize code re-use `4 marks`
  - SOLID principles & Law of Demeter
- [ ] Submit a UML Diagram depicting appropriate use of OOP principles, inheritance `2 marks`
- [ ] Handle errors and unexpected behaviour (read: input) gracefully `1 mark`
- [ ] Format your output `1 mark`
  - make messages display the correct information in a pleasant, readable manner