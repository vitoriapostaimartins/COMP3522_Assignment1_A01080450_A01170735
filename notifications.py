"""
This module holds the the different types of notifications and warnings.
"""

from enum import Enum
from tabulate import tabulate


class Notifications(Enum):
    """
    Enum for notifications and warning messages. Stores the message strings as constants.
    """
    POLITE = tabulate([["Hey buddy, please be aware of your spendings :) You have exceeded the limit for this budget."]], tablefmt="fancy_grid")
    RUDE = tabulate([["You suck at managing your finances. You have exceeded the limit for this budget."]], tablefmt="fancy_grid")
    WARNING = tabulate([["Warning! You getting close to your budget limit"]], tablefmt="fancy_grid")
