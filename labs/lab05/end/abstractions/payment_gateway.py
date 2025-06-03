from abc import ABC, abstractmethod


class PaymentGateway(ABC):
    """
    Abstraction for charging payments. High-level modules depend on this.
    """
    @abstractmethod
    def charge(self, credit_card_number: str, amount: float) -> bool:
        pass
