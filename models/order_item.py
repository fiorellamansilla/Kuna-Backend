from models.client import db

order_item = db.Table ("order_item",
    db.Column ('order_item_id', db.Integer, autoincrement = True, nullable =False, primary_key=True),
    db.Column ('order_id', db.Integer, db.ForeignKey ("orders.order_id", ondelete="CASCADE", onupdate="CASCADE"), nullable = False),
    db.Column ('item_id', db.Integer, db.ForeignKey ("item.item_id", ondelete="CASCADE", onupdate="CASCADE"), nullable = False),
    db.Column ('quantity_ordered', db.Integer, nullable = False, server_default="0"),
    db.Column ('total_amount', db.Float, nullable = False, server_default="0")
)




