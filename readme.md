Current Progress
================
- [x] **Show user menu**
  - View Budgets, Record Transaction, View Transactions by Budget, View Bank Account Details
- [ ] **Recording Transactions**
  - [x] Record & display transactions for a Budget
  - [x] Update Bank Account balance with each transaction
  - [ ] User cant record transaction that will cause balance to fall below 0
- [x] **User Registration**
  - register different User Types
- [ ] **Main Menu**
  - display on startup
  ```python
    1 - Register new user
    2 - Login
    3 - Exit
  ```
- [ ] **User Login**
  - store registered users in list, allow login functionality
- [ ] **Login Menu**
  - display if login chosen from main menu
  ```python
    1 - Jeff (Rebel)
    2 - Mike (Troublemaker)
    3 - Shachi (Angel)
    4 - Back to main menu
  ```
- [ ] **Notifications**
  - [ ] Enum to store message types
  - [ ] Perform check after transaction to see if warning or notification should be issued
    - [ ] Notify if exceed budget category
         - polite or rude message
    - [ ] Warning if exceed a % of budget
      - Angel: >90%
      - Troublemaker: >70%
      - Rebel: >50%
    - [ ] Print list of transactions
        - After warning that they are close to exceeding budget for a category
        - After notification that they have exceeded budget for a category
- [ ] **Lockout - Budget**
  - for Troublemaker and Rebel
  - [ ] Lock out from recording transactions (i.e. spending money)
    - Troublemaker: if exceed >120%
    - Rebel: if exceed >100%
  - [ ] Notify via console message
  - [ ] Deny attempts at recording transactions in affected budget
- [ ] **Lockout - Account (Rebel)**
    - exceed budget in 2+ categories = lock out from account