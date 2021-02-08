"""
This module houses the FAM - the controller of the program.
"""

from user import User
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
        ## user name, age, type bank account number, bank name, bank balance, their budgets
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

        self.add_user_to_list(user)

    @property
    def user_list(self):
        """
        Retrieve the FAM user list.
        :return: the user list as an array
        """
        return self._user_list

    def show_actions_menu(self):
        """
        Show the actions menu and takes input from the user.
        :return:
        """
        while True:
            # options:
            print("""
            Actions menu:
            1 - View budgets
            2 - Record transaction
            3 - View transactions by budget
            4 - View bank account details
            5 - Quit
            """)

            option = int(input("Please enter the number your selection: "))
            # option 5 = QUIT = break the loop
            if option == 5:
                break

            # performs the action selected by the user.
            self.perform_action(option)

    def perform_action(self, option):
        """
        Perform an action based on the option selected by a user.
        :param option: an int
        """
        if option == 1:
            self.user_list[0].view_budgets()
        elif option == 2:
            self.user_list[0].record_transaction()
        elif option == 3:
            self.user_list[0].view_transactions()
        elif option == 4:
            self.user_list[0].view_bank_details()


def main():
    """
    Runner function of the FAM system.
    """

    fam = FAM()

    # registers a user
    fam.show_registration_menu()

    # shows the actions menu
    fam.show_actions_menu()


if __name__ == '__main__':
    main()
