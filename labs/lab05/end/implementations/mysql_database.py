from abstractions.database import Database


class MySqlDatabase(Database):
    """
    Concrete implementation of IDatabase for MySQL.
    """
    def connect(self) -> None:
        print("[MySqlDatabase] Connected to MySQL database.")

    def save_order(self, order_id: int, amount: float) -> None:
        print(f"[MySqlDatabase] Order {order_id} with amount ${amount:.2f} saved to MySQL database.")

    def get_order(self, order_id: int):
        print(f"[MySqlDatabase] Retrieving Order {order_id} from MySQL database.")
        return {"order_id": order_id, "amount": 99.99}
