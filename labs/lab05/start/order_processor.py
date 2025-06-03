from my_sql_database import MySqlDatabase
from email_notifier import EmailNotifier
from payment_gateway import PaymentGateway


class OrderProcessor:
    """
    High-level business logic that depends directly on low-level classes.
    """
    def __init__(self):
        # Violating DIP: directly instantiating concrete classes
        self._db = MySqlDatabase()
        self._notifier = EmailNotifier()
        self._payment_gateway = PaymentGateway()

    def process_order(self, order_id: int, credit_card_number: str, amount: float, customer_email: str):
        # Step 1: Charge the card
        print(f"[OrderProcessor] Starting processing for order {order_id}.")
        payment_success = self._payment_gateway.charge(credit_card_number, amount)

        if payment_success:
            # Step 2: Save order to DB
            self._db.connect()
            self._db.save_order(order_id, amount)

            # Step 3: Send notification email
            subject = f"Order #{order_id} Confirmation"
            body = f"Your order of ${amount:.2f} has been successfully placed."
            self._notifier.send_email(customer_email, subject, body)
            print(f"[OrderProcessor] Order {order_id} processed successfully.")
        else:
            print(f"[OrderProcessor] Payment for order {order_id} failed. Aborting.")
            