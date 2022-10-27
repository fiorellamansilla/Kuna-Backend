from datetime import datetime

class User:
    # Constructor
    def __init__(self, username=None, password_hash="", email=None, country=None):
        self.username = username
        self.password_hash = password_hash
        self.email = email
        self.country = country
        self.is_blocked = False
        self.is_approved = False
        self.created_at = datetime.today().isoformat()

    def __repr__(self):
        return str(self.__dict__)
