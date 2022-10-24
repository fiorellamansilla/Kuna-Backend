from enums.color import Color
from enums.size import Size

class Item:
    def __init__(self,item_schema):
        self.item_id = item_schema['item_id']
        self.name_item = item_schema['name_item']
        self.desc_item = item_schema['desc_item']
        self.size = Size(item_schema['size'])
        self.color = Color(item_schema['color'])
        self.price = item_schema['price']
        self.discount = item_schema['discount']
        self.SKU = item_schema['SKU']
        self.quantity_stock = item_schema['quantity_stock']
        self.image_path = item_schema['image_path']
        self.created_at = item_schema['created_at']
        self.modified_at = item_schema['modified_at']
        self.deleted_at = item_schema['deleted_at']

    def __repr__(self):
        return str(self.__dict__)

    def toJSON(self):      
        return str(self.__dict__)

