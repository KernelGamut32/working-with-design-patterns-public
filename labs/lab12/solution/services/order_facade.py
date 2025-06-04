from pizza.pizza import Pizza
from services.inventory import InventoryService
from services.loyalty import LoyaltyService
from services.payment import PaymentProcessor
from services.delivery import DeliveryService

class OrderFacade:
    """
    Facade that simplifies the pizza ordering process by coordinating:
      1. Inventory check/reservation
      2. Loyalty discount application
      3. Payment processing
      4. Delivery scheduling
    """
    def __init__(self):
        self._inventory = InventoryService()
        self._loyalty = LoyaltyService()
        self._payment = PaymentProcessor()
        self._delivery = DeliveryService()

    def place_order(self, pizza: Pizza, toppings: list, address: str, email: str = None) -> bool:
        """
        Orchestrates the entire order:
         - Check & reserve inventory
         - Apply loyalty discount (if applicable)
         - Process payment
         - Schedule delivery
        Returns True if order is successful; otherwise False.
        """
        # 1. Inventory
        pizza_desc = pizza.get_description().split(" (")[0]  # e.g., "Margherita Pizza"
        if not self._inventory.check_and_reserve(pizza_desc, toppings):
            print("[OrderFacade] Order failed: inventory issue.")
            return False

        # 2. Loyalty
        total_cost = pizza.get_cost()
        total_cost = self._loyalty.apply_discount(email, total_cost)
        if not total_cost:
            print("[OrderFacade] Order failed: loyalty discount application failed.")
            return False
        if total_cost <= 0:
            print("[OrderFacade] Order failed: invalid total cost after discount.")
            return False

        # 3. Payment
        print(f"[OrderFacade] Total cost to charge: ${total_cost:.2f}")
        if not self._payment.process_payment(total_cost):
            print("[OrderFacade] Order failed: payment declined.")
            return False

        # 4. Delivery
        tracking_id = self._delivery.schedule_delivery(address)
        print(f"[OrderFacade] Order success! Your pizza is on the way. Tracking ID: {tracking_id}")
        return True
    