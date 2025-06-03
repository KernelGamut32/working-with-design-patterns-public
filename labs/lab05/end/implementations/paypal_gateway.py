from abstractions.payment_gateway import PaymentGateway


class PaypalGateway(PaymentGateway):
    """
    Concrete implementation of IPaymentGateway using PayPal.
    """
    def charge(self, credit_card_number: str, amount: float) -> bool:
        print(f"[PaypalGateway] Charging ${amount:.2f} to card {credit_card_number} via PayPal.")
        return False  # Simulate a failure for demonstration
    