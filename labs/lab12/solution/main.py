from pizza.pizza import MargheritaPizza, NeapolitanPizza
from pizza.toppings import Cheese, Olives, Pepperoni, Mushrooms, Bacon
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
    print(f"Cost (Before Loyalty Discount): ${pizza_with_toppings_1.get_cost():.2f}")
    facade.place_order(pizza_with_toppings_1, toppings_list_1, address_1)
    print()

    # Example 2: Neapolitan + Cheese + Mushrooms + Pepperoni
    base_pizza_2 = NeapolitanPizza()
    pizza_with_toppings_2 = Pepperoni(Mushrooms(Cheese(base_pizza_2)))
    toppings_list_2 = ["Pepperoni", "Mushrooms", "Extra Cheese"]
    address_2 = "456 Elm St, Shelbyville"

    print("---- Placing Order 2 ----")
    print(f"Description: {pizza_with_toppings_2.get_description()}")
    print(f"Cost (Before Loyalty Discount): ${pizza_with_toppings_2.get_cost():.2f}")
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
    print(f"Cost (Before Loyalty Discount): ${pricey.get_cost():.2f}")
    facade.place_order(pricey, toppings_list_3, address_3)
    print()

    # Example 4: Neapolitan + Bacon + Olives
    base_pizza_4 = NeapolitanPizza()
    pizza_with_toppings_4 = Bacon(Olives(base_pizza_4))
    toppings_list_4 = ["Bacon", "Olives"]
    address_4 = "1010 Maple Rd, Capital City"

    print("---- Placing Order 4 ----")
    print(f"Description: {pizza_with_toppings_4.get_description()}")
    print(f"Cost (Before Loyalty Discount): ${pizza_with_toppings_4.get_cost():.2f}")
    facade.place_order(pizza_with_toppings_4, toppings_list_4, address_4, "bob@example.com")
    print()

    # Example 5: Margherita + Cheese + Bacon + Loyalty Discount
    base_pizza_5 = MargheritaPizza()
    pizza_with_toppings_5 = Bacon(Cheese(base_pizza_4))
    toppings_list_5 = ["Cheese", "Bacon"]
    address_5 = "1313 Mockingbird Lane, Gotham City"

    print("---- Placing Order 5 ----")
    print(f"Description: {pizza_with_toppings_5.get_description()}")
    print(f"Cost (Before Loyalty Discount): ${pizza_with_toppings_5.get_cost():.2f}")
    facade.place_order(pizza_with_toppings_5, toppings_list_5, address_5, "alice@example.com")
    print()

if __name__ == "__main__":
    main()
