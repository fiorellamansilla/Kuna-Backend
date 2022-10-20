from enums.color_item import Color
from enums.size_item import Size
import json


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

    def toJSON(self):
        return "item {}: {}, {}, {}, {}, {}, {}, {}, {}, {}".format(self.item_id,self.name_item, self.desc_item, self.size.value, self.color.value, self.price, self.discount, self.SKU, self.quantity_stock, self.image_path)

    def __repr__(self):
        return '' % self.item_id


