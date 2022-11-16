
class OrderItemEntity:

    def __init__(self, order_item_schema):
        self.order_item_id = order_item_schema['order_item_id']
        self.quantity_ordered = order_item_schema['quantity_ordered']
        self.total_amount = order_item_schema['total_amount']

    def __repr__(self):
        return str(self.__dict__)

    def toJSON(self):      
        return str(self.__dict__)