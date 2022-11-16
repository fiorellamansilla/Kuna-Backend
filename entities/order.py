
class Order:
    
    def __init__(self, order_schema):
        self.order_id = order_schema['order_id']
        self.order_amount = order_schema['order_amount']
        self.client_id = order_schema['client_id']
        self.ship_name = order_schema['ship_name']
        self.ship_address = order_schema['ship_address']
        self.order_city = order_schema['order_city']
        self.order_zip = order_schema['order_zip']
        self.order_country = order_schema['order_country']
        self.order_phone = order_schema['order_phone']
        self.order_email = order_schema['order_email']
        self.ordered_at = order_schema['ordered_at']
        self.shipped_at = order_schema['shipped_at']
        self.tracking_number = order_schema['tracking_number']
        
    def __repr__(self):
        return str(self.__dict__)

    def toJSON(self):      
        return str(self.__dict__)