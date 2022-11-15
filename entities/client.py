
class Client:
    
    def __init__(self, client_schema):
        self.client_id = client_schema['client_id']
        self.username = client_schema ['username']
        self.password_client = client_schema ['password_client']
        self.first_name = client_schema ['first_name']
        self.last_name = client_schema ['last_name']
        self.address_client = client_schema ['address_client']
        self.zip_code = client_schema ['zip_code']
        self.city = client_schema ['city']
        self.country = client_schema ['country']
        self.phone = client_schema ['phone']
        self.email = client_schema ['email']
        self.created_at = client_schema['created_at']
        self.modified_at = client_schema['modified_at']

    def __repr__(self):
        return str(self.__dict__)

    def toJSON(self):      
        return str(self.__dict__)

