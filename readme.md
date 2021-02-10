Current Progress
================
- [x] **Show user menu**
  - View Budgets, Record Transaction, View Transactions by Budget, View Bank Account Details
- [ ] **Recording Transactions**
  - [ ] Record & display transactions for a Budget
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
  - Enum to store message types
  - notify if exceed budget category
    - polite or rude message
  - warning if exceed a % of budget
    - Angel: >90%
    - Troublemaker: >70%
    - Rebel: >50%
- [ ] **Lockout - Budget**
  - for Troublemaker and Rebel
  - lock out from recording transactions (i.e. spending money)
    - Troublemaker: if exceed >120%
    - Rebel: if exceed >100%
  - notify via console message
  - deny attempts at recording transactions in affected budget
- [ ] **Lockout - Account (Rebel)**
    - exceed budget in 2+ categories = lock out from account