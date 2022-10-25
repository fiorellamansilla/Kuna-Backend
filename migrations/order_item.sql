USE kuna_db;

CREATE TABLE order_item (
order_id INT NOT NULL,
item_id INT NOT NULL,
FOREIGN KEY (order_id) REFERENCES orders(order_id),
FOREIGN KEY (item_id) REFERENCES item(item_id),
UNIQUE (order_id, item_id)
);