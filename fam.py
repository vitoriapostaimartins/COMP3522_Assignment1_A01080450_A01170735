"""
This module houses the FAM - contains the UI of the program.
"""

from user import User, UserIsLockedError
from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel


class FAM:
    """
    Class representing a Family Appointed Moderator (F.A.M.)
    """

    def __init__(self):
        """
        Initialize the user list.
        """
        self._user_list = []
        self._current_user = None

    @property
    def current_user(self):
        """
        Get the user that is currently logged in.
        :return: a User
        """
        return self._current_user

    @current_user.setter
    def current_user(self, user):
        """
        Set the user that is currently logged in.
        :param user: a User
        """
        self._current_user = user

    @property
    def user_list(self):
        """
        Retrieve the FAM user list.
        :return: the user list as a list
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        """
        Set the user list to the value passed in.
        :param user_list: a list of Users
        """
        self._user_list = user_list

    def _add_user_to_list(self, user):
        """
        Add a user to the list.
        :param user: the User object to be added to the list of users
        """
        self._user_list.append(user)

    def _show_registration_menu(self):
        """
        Show the menu for registering a new user to the system.
        """

        # register the user
        self.register_user()

    def _register_user(self):
        """
        Prompt user to enter their details and add them to the user list.
        :return: True always
        """
        print("\n       Register a new user")
        print("----------------------------------")
        print("Complete the following details for registration")
        while True:
            try:
                user_name = input("Enter your Name:")
                user_age = int(input("Enter your Age:"))
                user_type = int(input("""Enter your User Type:
                                  1 - Angel
                                  2 - Troublemaker
                                  3 - Rebel
                                  """))
            except ValueError as e:
                print("Please input age and user type as integers")
                continue

            if user_type == 1:
                user = Angel(user_name, user_age)
                break
            elif user_type == 2:
                user = Troublemaker(user_name, user_age)
                break
            elif user_type == 3:
                user = Rebel(user_name, user_age)
                break
            else:
                print("\nPlease try again and choose a valid user type.")

        self.current_user = user
        self._add_user_to_list(user)

        return True

    def _show_actions_menu(self):
        """
        Show the actions menu and takes input from the user.
        """
        while True:
            # Check if a user is locked, if so exit out of the actions menu
            print("locked:", self.current_user.locked_budgets)
            if self.current_user.can_lock_account():
                raise UserIsLockedError("Your account is locked. We have logged you out")

            print(f"\nLogged in as {self.current_user.name}")

            # options:
            print("""
            Actions menu:
            1 - View budgets
            2 - Record transaction
            3 - View transactions by budget
            4 - View bank account details
            5 - Logout
            """)

            try:
                option = int(input("Please enter the number your selection: "))
            except ValueError:
                print("Invalid choice. Please try again.")
                continue
            # option 5 = LOGOUT, back to main menu
            if option == 5:
                return
            else:
                # performs the action selected by the user.
                self.perform_action(option)

    def _perform_action(self, option):
        """
        Perform an action based on the option selected by a user.
        :param option: an int
        """
        if option == 1:
            self.current_user.view_budgets()
        elif option == 2:
            self.current_user.record_transaction()
        elif option == 3:
            self.current_user.view_transactions()
        elif option == 4:
            self.current_user.view_bank_details()
        else:
            print("Please enter a valid option.")

    def _login_user(self):
        """
        Select a user from the user list to log in.
        :return: True if the login process succeeds, False otherwise
        """
        # Display list of users and prompt an input
        print("---- Login Menu ----")
        for user in self.user_list:
            print(f"{self.user_list.index(user) + 1} - {user}")

        # Exit if the last option is chosen
        choice_exit = len(self.user_list) + 1
        print(f"{choice_exit} - Back to main menu")

        valid_users = range(1, len(self.user_list) + 1)
        choice = 0
        while True:
            try:
                choice = int(input("Choose a user by entering the id: "))
            except ValueError:
                print("Invalid choice. Please try again.")
                continue

            # Loop until a valid user is selected
            if choice in valid_users:
                break
            elif choice == choice_exit:
                return False
            else:
                print("Please enter a valid option")

        # Set current user to selected user
        self.current_user = self.user_list[choice - 1]
        return True

    def show_main_menu(self):
        """
        Show the main menu with options to register a new user,
        login, or exit the FAM application.
        """

        # Display a welcome message
        print("""          
       ___                       
     /'___\                      
    /\ \__/   __      ___ ___    
    \ \ ,__\/'__`\  /' __` __`\  
     \ \ \_/\ \L\.\_/\ \/\ \/\ \ 
      \ \_\\ \__/.\_\ \_\ \_\ \_\\
       \/_/ \/__/\/_/\/_/\/_/\/_/      
              """)
        print("       Family Appointed Moderator")
        print("----------------------------------------")

        # Prompt user to register, login, or exit the F.A.M until they choose a valid option.
        while True:

            print("""
            1 - Register new user
            2 - Login
            3 - Exit
                  """)

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid choice. Please try again.")
                continue

            if choice == 3:
                return
            elif choice > 3 or choice < 0:
                print("Invalid choice. Please try again.")
            else:
                input_map = {
                    1: self.register_user,
                    2: self.login_user,
                }

                # Catch any string values
                try:
                    operation = input_map[choice]
                except ValueError:
                    print("Invalid choice. Please try again.")
                    continue

                # Move to the actions menu after a user is logged in or registered
                if operation():
                    try:
                        self._show_actions_menu()
                    except UserIsLockedError as e:
                        print(e)

    @staticmethod
    def load_test_user():
        """
        Return a test user for developing purposes.
        return: a test user as a User object
        """
        return Angel("Bob", 25)
