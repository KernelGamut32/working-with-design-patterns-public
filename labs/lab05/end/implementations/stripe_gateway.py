from abstractions.payment_gateway import PaymentGateway


class StripeGateway(PaymentGateway):
    """
    Concrete implementation of IPaymentGateway using Stripe.
    """
    def charge(self, credit_card_number: str, amount: float) -> bool:
        print(f"[StripeGateway] Charging ${amount:.2f} to card {credit_card_number} via Stripe.")
        return True  # Simulate success
