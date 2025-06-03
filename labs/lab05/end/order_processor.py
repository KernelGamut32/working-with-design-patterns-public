from typing import Dict, Any
from abstractions.database import Database
from abstractions.notifier import Notifier
from abstractions.payment_gateway import PaymentGateway


class OrderProcessor:
    """
    High-level business logic, now depending only on IDatabase, INotifier, IPaymentGateway.
    """

    def __init__(
        self,
        db: Database,
        notifier: Notifier,
        payment_gateway: PaymentGateway
    ):
        """
        Dependencies are injected via constructor (inversion of control).
        """
        self._db = db
        self._notifier = notifier
        self._payment_gateway = payment_gateway

    def process_order(
        self,
        order_id: int,
        credit_card_number: str,
        amount: float,
        customer_contact: str
    ) -> None:
        print(f"[OrderProcessor] Starting processing for order {order_id}.")

        # Charge the payment (depends only on IPaymentGateway)
        payment_success = self._payment_gateway.charge(credit_card_number, amount)

        if not payment_success:
            print(f"[OrderProcessor] Payment for order {order_id} failed. Aborting.")
            return

        # Persist order (depends only on IDatabase)
        self._db.connect()
        self._db.save_order(order_id, amount)

        # Send notification (depends only on INotifier)
        subject = f"Order #{order_id} Confirmation"
        body = f"Your order of ${amount:.2f} has been successfully placed."
        self._notifier.send(customer_contact, subject, body)

        print(f"[OrderProcessor] Order {order_id} processed successfully.")

    def lookup_order(self, order_id: int) -> Dict[str, Any]:
        """
        Example of another high-level operation: fetching an order.
        """
        self._db.connect()
        return self._db.get_order(order_id)
