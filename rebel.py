from notifications import Notifications
from user import User


class Rebel(User):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_type(self):
        return "Rebel"

    def get_notification(self):
        return Notifications.RUDE.value
