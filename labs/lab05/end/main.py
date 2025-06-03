from abstractions.database import Database
from abstractions.notifier import Notifier
from abstractions.payment_gateway import PaymentGateway
from implementations.mysql_database import MySqlDatabase
from implementations.postgres_database import PostgresDatabase
from implementations.email_notifier import EmailNotifier
from implementations.sms_notifier import SmsNotifier
from implementations.stripe_gateway import StripeGateway
from implementations.paypal_gateway import PaypalGateway
from order_processor import OrderProcessor


def main():
    # === Choose concrete implementations here ===
    # You can swap between MySqlDatabase or PostgresDatabase, EmailNotifier or SmsNotifier,
    # StripeGateway or PaypalGateway, without modifying OrderProcessor itself.

    db: Database = MySqlDatabase()
    notifier: Notifier = EmailNotifier()
    payment_gateway: PaymentGateway = StripeGateway()

    processor = OrderProcessor(db=db, notifier=notifier, payment_gateway=payment_gateway)

    # Process a successful order
    processor.process_order(
        order_id=1001,
        credit_card_number="4242-4242-4242-4242",
        amount=249.99,
        customer_contact="customer@example.com"
    )

    print("\n---\n")

    # Process an order with a failing payment (using PayPal)
    db2: Database = PostgresDatabase()           # swap to Postgres
    notifier2: Notifier = SmsNotifier()           # swap to SMS
    payment_gateway2: PaymentGateway = PaypalGateway()  # this one will simulate failure

    processor2 = OrderProcessor(db=db2, notifier=notifier2, payment_gateway=payment_gateway2)
    processor2.process_order(
        order_id=1002,
        credit_card_number="5555-5555-5555-4444",
        amount=79.50,
        customer_contact="555-123-4567"
    )

    print("\n--- Lookup an order that was saved earlier ---")
    order_data = processor.lookup_order(order_id=1001)
    print(f"Fetched Order Data: {order_data}")

if __name__ == "__main__":
    main()
