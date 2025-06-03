from abc import ABC, abstractmethod


class Notifier(ABC):
    """
    Abstraction for notification. High-level modules depend on this.
    """
    @abstractmethod
    def send(self, recipient: str, subject: str, body: str) -> None:
        pass
