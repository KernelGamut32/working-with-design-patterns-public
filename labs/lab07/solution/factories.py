from abc import ABC, abstractmethod
from products import Button, TextField, Checkbox, Label

class GUIFactory(ABC):
    @abstractmethod
    def create_button(self, caption: str) -> Button:
        pass

    @abstractmethod
    def create_textfield(self, placeholder: str) -> TextField:
        pass

    @abstractmethod
    def create_checkbox(self, label: str) -> Checkbox:
        pass

    @abstractmethod
    def create_label(self, text: str) -> Label:
        pass

def get_factory(theme: str) -> GUIFactory:
    theme = theme.strip().lower()
    if theme == "light":
        from light_theme import LightThemeFactory
        return LightThemeFactory()
    elif theme == "dark":
        from dark_theme import DarkThemeFactory
        return DarkThemeFactory()
    elif theme == "blue":
        from blue_theme import BlueThemeFactory
        return BlueThemeFactory()
    else:
        raise ValueError(f"Unsupported theme '{theme}'.")
    