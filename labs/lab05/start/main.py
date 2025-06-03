from order_processor import OrderProcessor


def main():
    processor = OrderProcessor()
    # Hard-coded credit card and email—no way to change DB/notifier without editing OrderProcessor
    processor.process_order(
        order_id=1234,
        credit_card_number="4111-1111-1111-1111",
        amount=149.95,
        customer_email="customer@example.com"
    )


if __name__ == "__main__":
    main()
