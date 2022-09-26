USE kuna_db;

CREATE TABLE items (
item_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
name_item VARCHAR(128) NOT NULL,
desc_item VARCHAR (2048) NOT NULL ,
size VARCHAR(64) NOT NULL,
price FLOAT NOT NULL DEFAULT 0,
discount FLOAT NOT NULL DEFAULT 0,
SKU VARCHAR (128) NOT NULL,
quantity_stock INT NOT NULL DEFAULT 0
);

INSERT INTO items (item_id, name_item, desc_item, size, price, SKU, quantity_stock) 
VALUES (1, 'Body Clásico', 'Body de algodón orgánico para bebé recién nacido.', '0 - 3m', 50.00, '19293119', 5); 

INSERT INTO items (item_id, name_item, desc_item, size, price, SKU, quantity_stock) 
VALUES (2, 'Vestido Cashmere', 'Vestido de punto para niña con bajo en ondas a contraste en color blanco.', '3 - 6m', 80.00, '19293120', 3); 
 



