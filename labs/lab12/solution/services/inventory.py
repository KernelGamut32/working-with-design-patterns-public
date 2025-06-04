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
    