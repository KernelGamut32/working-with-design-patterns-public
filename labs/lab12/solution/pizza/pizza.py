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
    