USE kuna_db;

CREATE TABLE  order_item (
order_item_id INT NOT NULL AUTO_INCREMENT,
order_id INT NOT NULL,
item_id INT NOT NULL,
quantity_ordered INT NOT NULL DEFAULT 0,
total_amount FLOAT NOT NULL DEFAULT 0,
PRIMARY KEY (order_item_id),
FOREIGN KEY (order_id) REFERENCES orders(order_id) ON DELETE CASCADE ON UPDATE CASCADE,
FOREIGN KEY (item_id) REFERENCES item(item_id) ON DELETE CASCADE ON UPDATE CASCADE
);