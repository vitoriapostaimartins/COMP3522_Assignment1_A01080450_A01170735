"""
This module holds the driver function for the FAM program.
"""
from fam import FAM


def main():
    """
    Driver for the FAM system.
    """

    fam = FAM()

    # show main menu
    fam.show_main_menu()


if __name__ == '__main__':
    main()
