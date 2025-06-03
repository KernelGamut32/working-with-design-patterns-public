from products import Button, TextField, Checkbox, Label
from factories import GUIFactory

class DarkButton(Button):
    def __init__(self, caption: str):
        self.caption = caption

    def render(self) -> None:
        print(f"[Dark Button] [ {self.caption} ] rendered with black background, white text.")

    def on_click(self) -> None:
        print(f"[Dark Button] '{self.caption}' was clicked. (Dark theme style)")

class DarkTextField(TextField):
    def __init__(self, placeholder: str):
        self.placeholder = placeholder
        self.text = ""

    def render(self) -> None:
        print(f"[Dark TextField] <{self.placeholder}> rendered with black background, white border.")

    def get_input(self) -> str:
        self.text = f"UserInput_for_{self.placeholder}"
        print(f"[Dark TextField] Received input: '{self.text}'")
        return self.text

class DarkCheckbox(Checkbox):
    def __init__(self, label: str):
        self.label = label
        self.checked = False

    def render(self) -> None:
        state = "✔" if self.checked else " "
        print(f"[Dark Checkbox] [ {state} ] {self.label} (black background)")

    def toggle(self) -> bool:
        self.checked = not self.checked
        print(f"[Dark Checkbox] '{self.label}' toggled to {'checked' if self.checked else 'unchecked'}.")
        return self.checked
    
class DarkLabel(Label):
    def __init__(self, text: str):
        self.text = text

    def render(self) -> None:
        print(f"[Dark Label] {self.text} (black background)")

class DarkThemeFactory(GUIFactory):
    def create_button(self, caption: str) -> Button:
        return DarkButton(caption)

    def create_textfield(self, placeholder: str) -> TextField:
        return DarkTextField(placeholder)

    def create_checkbox(self, label: str) -> Checkbox:
        return DarkCheckbox(label)
    
    def create_label(self, text: str) -> Label:
        return DarkLabel(text)
    