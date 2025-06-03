from abstractions.database import Database


class PostgresDatabase(Database):
    """
    Concrete implementation of IDatabase for PostgreSQL.
    """
    def connect(self) -> None:
        print("[PostgresDatabase] Connected to PostgreSQL database.")

    def save_order(self, order_id: int, amount: float) -> None:
        print(f"[PostgresDatabase] Order {order_id} with amount ${amount:.2f} saved to PostgreSQL database.")

    def get_order(self, order_id: int):
        print(f"[PostgresDatabase] Retrieving Order {order_id} from PostgreSQL database.")
        return {"order_id": order_id, "amount": 199.99}
    