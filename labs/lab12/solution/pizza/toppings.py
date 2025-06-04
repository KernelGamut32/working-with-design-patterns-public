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


class Bacon(ToppingDecorator):
    """
    Concrete Decorator: Bacon topping.
    """
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Bacon"

    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.75  # Bacon costs $1.75
    