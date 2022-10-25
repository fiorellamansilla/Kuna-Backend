from datetime import datetime
import hashlib

CONST_SALT = "5gz"

class User:
    # Constructor
    def __init__(self, username=None, password="", email=None, country=None):
        p = password + CONST_SALT
        self.username = username
        self.__password_hash = hashlib.md5(p.encode()).hexdigest()
        self.email = email
        self.country = country
        self.is_blocked = False
        self.is_approved = True
        self.creation_date = datetime.today().isoformat()
        self.purchased_items = 0

    def __repr__(self):
        return str(self.__dict__)

    def change_password(self, new_password):
        p = new_password + CONST_SALT
        self.__password_hash = hashlib.md5(p.encode().hexdigest())

    def change_country(self, new_country):
        self.country = new_country

    def change_email(self, new_email):
        self.email = new_email

    def buy_something(self):
        self.purchased_items = self.purchased_items + 1

    def get_password(self):
        return self.__password_hash

    def is_correct_password(self, password_attempt):
        p = password_attempt + CONST_SALT
        hashed_attempt = hashlib.md5(p.encode())
        return hashed_attempt.hexdigest() ==  self.__password_hash