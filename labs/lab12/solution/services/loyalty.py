class LoyaltyService:
    """
    Simulates a loyalty program that applies a percentage discount.
    """
    def __init__(self):
        # Example: a simple “loyalty points” storage
        self._points = {"alice@example.com": 120, "bob@example.com": 45}

    def apply_discount(self, email: str, amount: float) -> float:
        """
        Reduce the amount by 5% if points ≥ 100, otherwise no discount.
        """
        if self._points.get(email, 0) >= 100:
            discount = amount * 0.05
            print(f"[LoyaltyService] Applied 5% discount (${discount:.2f}) for {email}.")
            return amount - discount
        else:
            print(f"[LoyaltyService] No discount for {email}.")
            return amount
