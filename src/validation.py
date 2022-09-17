#Validate item_id as an integer

def validate_item_id(item_id: int) -> bool:
    if item_id >= 1 and item_id <= 1000000:
        return True
    else:
        return False

#Validate name_item as a string with max 128 char. 

def validate_name_item(name_item: str) -> bool:
    name_item = name_item.strip()
    return (len(name_item) > 0 and len(name_item) <= 128)

#Validate desc_item as a string with max 2048 char.

def validate_desc_item(desc_item: str) -> bool:
    desc_item = desc_item.strip()
    return (len(desc_item) > 0 and len(desc_item) <= 2048)

#Validate size as a string with max 64 char.

def validate_size(size: str) -> bool:
    size = size.strip()
    return (len(size) > 0 and len(size) <= 64)

#Validate price as a float 

def validate_price(price:float) -> bool:
    if price >= 1 and price <= 100000:
        return True
    else:
        return False

#Validate discount as a float 

def validate_discount(discount:float) -> bool:
    if discount >= 1 and discount <= 1000:
        return True
    else:
        return False

# Validate SKU as a string with max 128 char.

def validate_SKU(SKU: str) -> bool:
    SKU = SKU.strip()
    return (len(SKU) > 0 and len(SKU) <= 128)

#Validate quantity_stock as a small integer between 1 and 8 digits

def validate_quantity_stock(quantity_stock:int) -> bool:
    if quantity_stock >= 1 and quantity_stock <= 10000000:
        return True
    else:
        return False

