from base import BaseClass


class User(BaseClass):
    def __init__(self, firstname, lastname, phone_number, *args, **kwargs):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
        super().__init__(*args, **kwargs)

    def full_name(self):
        return f"name:{self.firstname} {self.lastname}"
