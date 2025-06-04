# Lab 12 - Decorator & Facade Patterns

## Overview

In this lab, you will explore two fundamental design patterns in software engineering:

1. **Decorator Pattern:** Allows dynamic addition of responsibilities (toppings) to objects (pizzas) without modifying their original classes.
2. **Facade Pattern:** Provides a simplified interface (OrderFacade) to a set of complex subsystems (inventory, payment, delivery).

You’ll work through creating and understanding the provided code base, run sample scenarios, and then extend or modify the system to reinforce your understanding.

---

## Learning Objectives

By the end of this lab, you should be able to:

1. Explain the purpose and structure of the Decorator pattern.
2. Implement concrete decorator classes that wrap and augment a base component.
3. Explain the purpose and structure of the Facade pattern.
4. Build a facade that coordinates multiple subsystems behind a simple interface.
5. Modify and extend the existing code to add new functionality (e.g., new toppings, new payment logic).
6. Trace the flow of control when applying decorators and when invoking the facade.

---

## Prerequisites

Before you begin, ensure the following:

1. Python 3.8+ installed - Confirm by running `python --version` in your terminal.
2. An editor or IDE capable of editing multiple `.py` files (e.g., VS Code, PyCharm, Sublime Text).
3. Familiarity with basic OOP in Python - You should know what classes, methods, and imports/modules are.
4. Basic comfort with the command line - You’ll navigate directories and launch Python scripts.

---

## File Structure

Create a new folder on your local machine (e.g., `pizza_app/`) which will contain the following structure:

```text
pizza_app/
├── pizza/
│   ├── __init__.py
│   ├── pizza.py
│   └── toppings.py
├── services/
│   ├── __init__.py
│   ├── inventory.py
│   ├── payment.py
│   ├── delivery.py
│   └── order_facade.py
└── main.py
```

---

## Examine the Code

pizza/pizza.py

```python
from abc import ABC, abstractmethod

class Pizza(ABC):
    """
    The Component interface for pizzas.
    Defines methods to get description and cost.
    """
    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


class MargheritaPizza(Pizza):
    """
    A concrete pizza: Margherita.
    """
    def get_description(self) -> str:
        return "Margherita Pizza (tomato sauce, mozzarella)"

    def get_cost(self) -> float:
        return 8.00  # base price


class NeapolitanPizza(Pizza):
    """
    A concrete pizza: Neapolitan.
    """
    def get_description(self) -> str:
        return "Neapolitan Pizza (tomato sauce, fresh mozzarella, basil)"

    def get_cost(self) -> float:
        return 10.00  # base price
```

pizza/toppings.py

```python
from abc import ABC, abstractmethod
from pizza.pizza import Pizza

class ToppingDecorator(Pizza, ABC):
    """
    The Decorator abstract class—wraps a Pizza instance.
    """
    def __init__(self, pizza: Pizza) -> None:
        self._pizza = pizza

    @abstractmethod
    def get_description(self) -> str:
        pass

    @abstractmethod
    def get_cost(self) -> float:
        pass


class Cheese(ToppingDecorator):
    """
    Concrete Decorator: Cheese topping.
    """
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Extra Cheese"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.25  # Cheese costs $1.25


class Olives(ToppingDecorator):
    """
    Concrete Decorator: Olives topping.
    """
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Olives"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.75  # Olives cost $0.75


class Pepperoni(ToppingDecorator):
    """
    Concrete Decorator: Pepperoni topping.
    """
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Pepperoni"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.50  # Pepperoni costs $1.50


class Mushrooms(ToppingDecorator):
    """
    Concrete Decorator: Mushrooms topping.
    """
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Mushrooms"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 0.90  # Mushrooms cost $0.90
```

services/inventory.py

```python
class InventoryService:
    """
    Simulates an inventory system that checks ingredient availability.
    """
    def __init__(self):
        # Simulate available items in stock
        self._inventory = {
            "tomato_sauce": 10,
            "mozzarella": 10,
            "basil": 5,
            "cheese": 10,
            "olives": 5,
            "pepperoni": 8,
            "mushrooms": 7
        }

    def check_and_reserve(self, pizza_type: str, toppings: list) -> bool:
        """
        Check if all ingredients exist for the selected pizza type and toppings.
        If available, reserve (decrement) them and return True. Otherwise return False.
        """
        # Map pizza types to base ingredients
        pizza_ingredients = {
            "Margherita Pizza": ["tomato_sauce", "mozzarella"],
            "Neapolitan Pizza": ["tomato_sauce", "mozzarella", "basil"]
        }

        # Map topping names to inventory keys
        topping_map = {
            "Extra Cheese": "cheese",
            "Olives": "olives",
            "Pepperoni": "pepperoni",
            "Mushrooms": "mushrooms"
        }

        required = []

        # Base pizza ingredients
        if pizza_type in pizza_ingredients:
            required.extend(pizza_ingredients[pizza_type])
        else:
            print(f"[InventoryService] Unknown pizza type '{pizza_type}'.")
            return False

        # Add toppings ingredients
        for top in toppings:
            key = topping_map.get(top)
            if key:
                required.append(key)

        # Check availability
        for ingredient in required:
            if self._inventory.get(ingredient, 0) <= 0:
                print(f"[InventoryService] Ingredient '{ingredient}' is out of stock.")
                return False

        # Reserve (decrement) each ingredient
        for ingredient in required:
            self._inventory[ingredient] -= 1

        print(f"[InventoryService] Reserved ingredients for {pizza_type} with toppings {toppings}.")
        return True
```

services/payment.py

```python
class PaymentProcessor:
    """
    Simulates a payment processing subsystem.
    """
    def __init__(self):
        # In a real system, credentials and configuration would go here.
        pass

    def process_payment(self, amount: float) -> bool:
        """
        Process the payment of the given amount.
        Returns True if payment succeeds, False otherwise.
        """
        # Simulate: any amount under $100 succeeds; $100+ fails
        if amount < 100.00:
            print(f"[PaymentProcessor] Payment of ${amount:.2f} processed successfully.")
            return True
        else:
            print(f"[PaymentProcessor] Payment of ${amount:.2f} failed: exceeds limit.")
            return False
```

services/delivery.py

```python
import random
import time

class DeliveryService:
    """
    Simulates a delivery scheduling subsystem.
    """
    def __init__(self):
        # In a real system, this might connect to a delivery partner API.
        pass

    def schedule_delivery(self, address: str) -> str:
        """
        Schedule a delivery to the given address.
        Returns a delivery tracking ID.
        """
        # Simulate some processing delay
        time.sleep(0.5)

        # Generate a fake tracking ID
        tracking_id = f"DEL-{random.randint(1000,9999)}"
        print(f"[DeliveryService] Delivery scheduled to '{address}'. Tracking ID: {tracking_id}")
        return tracking_id
```

services/order_facade.py

```python
from pizza.pizza import Pizza
from services.inventory import InventoryService
from services.payment import PaymentProcessor
from services.delivery import DeliveryService

class OrderFacade:
    """
    Facade that simplifies the pizza ordering process by coordinating:
      1. Inventory check/reservation
      2. Payment processing
      3. Delivery scheduling
    """
    def __init__(self):
        self._inventory = InventoryService()
        self._payment = PaymentProcessor()
        self._delivery = DeliveryService()

    def place_order(self, pizza: Pizza, toppings: list, address: str) -> bool:
        """
        Orchestrates the entire order:
         - Check & reserve inventory
         - Process payment
         - Schedule delivery
        Returns True if order is successful; otherwise False.
        """
        # 1. Inventory
        pizza_desc = pizza.get_description().split(" (")[0]  # e.g., "Margherita Pizza"
        if not self._inventory.check_and_reserve(pizza_desc, toppings):
            print("[OrderFacade] Order failed: inventory issue.")
            return False

        # 2. Payment
        total_cost = pizza.get_cost()
        print(f"[OrderFacade] Total cost to charge: ${total_cost:.2f}")
        if not self._payment.process_payment(total_cost):
            print("[OrderFacade] Order failed: payment declined.")
            return False

        # 3. Delivery
        tracking_id = self._delivery.schedule_delivery(address)
        print(f"[OrderFacade] Order success! Your pizza is on the way. Tracking ID: {tracking_id}")
        return True
```

main.py

```python
from pizza.pizza import MargheritaPizza, NeapolitanPizza
from pizza.toppings import Cheese, Olives, Pepperoni, Mushrooms
from services.order_facade import OrderFacade

def main():
    """
    Demonstrates the Decorator (toppings) and Facade (order process) patterns.
    """
    facade = OrderFacade()

    # Example 1: Margherita + Cheese + Olives
    base_pizza_1 = MargheritaPizza()
    pizza_with_toppings_1 = Cheese(Olives(base_pizza_1))
    toppings_list_1 = ["Extra Cheese", "Olives"]
    address_1 = "123 Main St, Springfield"

    print("---- Placing Order 1 ----")
    print(f"Description: {pizza_with_toppings_1.get_description()}")
    print(f"Cost: ${pizza_with_toppings_1.get_cost():.2f}")
    facade.place_order(pizza_with_toppings_1, toppings_list_1, address_1)
    print()

    # Example 2: Neapolitan + Cheese + Mushrooms + Pepperoni
    base_pizza_2 = NeapolitanPizza()
    pizza_with_toppings_2 = Pepperoni(Mushrooms(Cheese(base_pizza_2)))
    toppings_list_2 = ["Pepperoni", "Mushrooms", "Extra Cheese"]
    address_2 = "456 Elm St, Shelbyville"

    print("---- Placing Order 2 ----")
    print(f"Description: {pizza_with_toppings_2.get_description()}")
    print(f"Cost: ${pizza_with_toppings_2.get_cost():.2f}")
    facade.place_order(pizza_with_toppings_2, toppings_list_2, address_2)
    print()

    # Example 3: Very expensive pizza to demonstrate payment failure
    pricey = MargheritaPizza()
    for _ in range(80):  # each cheese adds $1.25 => 80 * 1.25 = $100
        pricey = Cheese(pricey)
    toppings_list_3 = ["Extra Cheese"] * 80
    address_3 = "789 Oak Ave, Ogdenville"

    print("---- Placing Order 3 (Expected Payment Failure) ----")
    print(f"Description: {pricey.get_description()}")
    print(f"Cost: ${pricey.get_cost():.2f}")
    facade.place_order(pricey, toppings_list_3, address_3)
    print()

if __name__ == "__main__":
    main()
```

To execute/test, run `python main.py`

---

## Additional Exercises (Time Permitting)

### Exercise 1: Add a New Topping (`Bacon`)

Create a new decorator class in `pizza/toppings.py` called `Bacon` that appends `", Bacon"` to
`get_description()` and adds $1.75 to `get_cost()`.

### Exercise 2: Add a New Subsystem for Loyalty Discount

Incorporate a new subsystem wrapped within the ordering facade that enables
application of a "loyalty discount" for returning customers. You could use a points value associated to each customer - if the customer has enough points accrued, a 5% discount can be applied as part of the ordering process. Include an `email` parameter in the `place_order` method that looks up the
number of points for a customer and applies the discount if a sufficient number has accrued.
