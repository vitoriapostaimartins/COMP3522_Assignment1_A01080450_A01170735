from enum import Enum


class Notifications(Enum):
    POLITE = "Hey buddy, please be aware of your spendings :) You have exceeded the limit for this budget."
    RUDE = "You suck at managing your finances. You have exceeded the limit for this budget."
    WARNING = "Warning! You getting close to your budget limit"
