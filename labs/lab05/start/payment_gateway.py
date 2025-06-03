class PaymentGateway:
    """
    Low-level payment gateway implementation.
    """
    def charge(self, credit_card_number: str, amount: float) -> bool:
        # Imagine this actually reaches out to a payment provider
        print(f"[PaymentGateway] Charging ${amount:.2f} to card {credit_card_number}.")
        # Let's assume every charge succeeds
        return True
