from entities.client import Client
from models.client import ClientSchema

class TestClient:
    def setup(self):
        client_schema = {
            "username": "username",
            "first_name": "test_name",
            "password_client": "password",
            "last_name": "last_name",
            "address_client": "address_client",
            "zip_code": "zip_code",
            "city": "city",
            "country": "country",
            "phone": "phone",
            "email": "email",
            "created_at": "some_date",
            "modified_at": "modified_at",
        }
        self.client = Client(client_schema)

    def test_creation(self):
        assert self.client is not None
        assert self.client.first_name == "test_name"
        assert self.client.city == "city"
        assert self.client.zip_code == "zip_code"
