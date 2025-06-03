from abc import ABC, abstractmethod

class Button(ABC):
    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def on_click(self) -> None:
        pass

class TextField(ABC):
    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def get_input(self) -> str:
        pass

class Checkbox(ABC):
    @abstractmethod
    def render(self) -> None:
        pass

    @abstractmethod
    def toggle(self) -> bool:
        pass

class Label(ABC):
    @abstractmethod
    def render(self) -> None:
        pass
    