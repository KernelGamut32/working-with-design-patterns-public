from abc import ABC, abstractmethod
from typing import Any, Dict


class Database(ABC):
    """
    Abstraction for data access. High-level modules depend on this.
    """
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def save_order(self, order_id: int, amount: float) -> None:
        pass

    @abstractmethod
    def get_order(self, order_id: int) -> Dict[str, Any]:
        pass
