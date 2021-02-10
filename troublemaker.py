from Assignments.Assignment1.notifications import Notifications
from user import User


class Troublemaker(User):
    def __init__(self, name, age):
        super().__init__(name, age, 70)

    def get_type(self):
        return "Troublemaker"

    def get_notification(self):
        return Notifications.POLITE.value
