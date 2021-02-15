"""
This module houses the FAM - the controller of the program.
"""

from user import User, UserIsLockedError
from angel import Angel
from troublemaker import Troublemaker
from rebel import Rebel


def load_test_user():
    """
    Return a test user for developing purposes.

    return: a test user as a User object
    """
    return User("Bob", 25)


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
        return self._current_user

    @current_user.setter
    def current_user(self, user):
        self._current_user = user

    def add_user_to_list(self, user):
        """
        Add a user to the list.
        :param user: the User object to be added to the list of users
        """
        self._user_list.append(user)

    def show_registration_menu(self):
        """
        Show the menu for registering a new user to the system.
        """

        # register the user
        self.register_user()

        # load test user
        # test_user = load_test_user()
        # self.add_user_to_list(test_user)

    def register_user(self):
        """

        :return:
        """
        print("Complete the following details for registration")
        user_name = input("Enter your Name:")
        user_age = int(input("Enter your Age:"))
        user_type = int(input("""Enter your User Type:
                          1 - Angel
                          2 - Troublemaker
                          3 - Rebel
                          """))

        if user_type == 1:
            user = Angel(user_name, user_age)
        elif user_type == 2:
            user = Troublemaker(user_name, user_age)
        elif user_type == 3:
            user = Rebel(user_name, user_age)

        self.current_user = user
        self.add_user_to_list(user)
        return True

    @property
    def user_list(self):
        """
        Retrieve the FAM user list.
        :return: the user list as an array
        """
        return self._user_list

    @user_list.setter
    def user_list(self, user_list):
        self._user_list = user_list

    def show_actions_menu(self):
        """
        Show the actions menu and takes input from the user.
        :return:
        """
        while True:
            # Check if a user is locked, if so exit out of the actions menu
            print("locked:", self.current_user.get_locked_budgets())
            if self.current_user.can_lock_account():
                raise UserIsLockedError("Your account is locked. We have logged you out")

            # options:
            print("""
            Actions menu:
            1 - View budgets
            2 - Record transaction
            3 - View transactions by budget
            4 - View bank account details
            5 - Logout
            """)

            option = int(input("Please enter the number your selection: "))
            # option 5 = LOGOUT, back to main menu
            if option == 5:
                return
            else:
                # performs the action selected by the user.
                self.perform_action(option)

    def perform_action(self, option):
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

    def login_user(self):
        """
        Select a user from the user list to log in.
        """
        # Display list of users and prompt an input
        print("---- Login Menu ----")
        for user in self.user_list:
            print(f"{self.user_list.index(user) + 1} - {user.name} ({user.get_type()})")

        # Exit if the last option is chosen
        choice_exit = len(self.user_list) + 1
        print(f"{choice_exit} - Back to main menu")

        valid_users = range(1, len(self.user_list) + 1)
        print(x for x in valid_users)

        while True:
            choice = int(input("Choose a user by entering the id: "))

            # Loop until a valid user is selected
            if choice in valid_users:
                break
            elif choice == choice_exit:
                return False
            else:
                print("Please enter a valid option")

        # Set current user to selected user
        self.current_user = self.user_list[choice - 1]
        print(f"\nLogged in as {self.current_user.name}")
        return True

    def show_main_menu(self):
        """
        Show the main menu with options to register a new user,
        login, or exit the FAM application.
        """
        # Prompt user to register or login
        while True:

            print("""
                    1 - Register new user
                    2 - Login
                    3 - Exit
                  """)

            choice = int(input("Enter your choice: "))

            if choice == 3:
                return
            elif 0 > choice > 3:
                print("Invalid")
            else:
                input_map = {
                    1: self.register_user,
                    2: self.login_user,
                }
                operation = input_map[choice]
                if operation():
                    try:
                        self.show_actions_menu()
                    except UserIsLockedError as e:
                        print(e)


def main():
    """
    Runner function of the FAM system.
    """

    fam = FAM()

    # show main menu
    fam.show_main_menu()

    # registers a user
    # fam.show_registration_menu()

    # shows the actions menu
    # fam.show_actions_menu()


if __name__ == '__main__':
    main()
