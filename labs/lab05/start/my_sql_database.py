class MySqlDatabase:
    """
    Low-level data access class for MySQL.
    """
    def connect(self):
        # Imagine this actually opens a real DB connection
        print("[MySqlDatabase] Connected to MySQL database.")

    def save_order(self, order_id: int, amount: float):
        # Imagine this actually executes an INSERT statement
        print(f"[MySqlDatabase] Order {order_id} with amount ${amount:.2f} saved to database.")

    def get_order(self, order_id: int):
        # Imagine this actually runs a SELECT
        print(f"[MySqlDatabase] Retrieving Order {order_id} from database.")
        return {"order_id": order_id, "amount": 99.99}
