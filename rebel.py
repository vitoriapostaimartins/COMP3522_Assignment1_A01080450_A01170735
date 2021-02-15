from notifications import Notifications
from user import User


class Rebel(User):
    def __init__(self, name, age):
        super().__init__(name, age, 50, True, 100)

    def can_lock_account(self):
        if super().get_locked_budgets() >= 2:
            return True
        return False

    def get_type(self):
        return "Rebel"

    def get_notification(self):
        return Notifications.RUDE.value
