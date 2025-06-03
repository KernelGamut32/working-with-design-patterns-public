from products import Button, TextField, Checkbox, Label
from factories import GUIFactory

class LightButton(Button):
    def __init__(self, caption: str):
        self.caption = caption

    def render(self) -> None:
        print(f"[Light Button] [ {self.caption} ] rendered with white background, black text.")

    def on_click(self) -> None:
        print(f"[Light Button] '{self.caption}' was clicked. (Light theme style)")

class LightTextField(TextField):
    def __init__(self, placeholder: str):
        self.placeholder = placeholder
        self.text = ""

    def render(self) -> None:
        print(f"[Light TextField] <{self.placeholder}> rendered with white background, black border.")

    def get_input(self) -> str:
        self.text = f"UserInput_for_{self.placeholder}"
        print(f"[Light TextField] Received input: '{self.text}'")
        return self.text

class LightCheckbox(Checkbox):
    def __init__(self, label: str):
        self.label = label
        self.checked = False

    def render(self) -> None:
        state = "X" if self.checked else " "
        print(f"[Light Checkbox] [ {state} ] {self.label} (white background)")

    def toggle(self) -> bool:
        self.checked = not self.checked
        print(f"[Light Checkbox] '{self.label}' toggled to {'checked' if self.checked else 'unchecked'}.")
        return self.checked
    
class LightLabel(Label):
    def __init__(self, text: str):
        self.text = text

    def render(self) -> None:
        print(f"[Light Label] {self.text} (white background)")

class LightThemeFactory(GUIFactory):
    def create_button(self, caption: str) -> Button:
        return LightButton(caption)

    def create_textfield(self, placeholder: str) -> TextField:
        return LightTextField(placeholder)

    def create_checkbox(self, label: str) -> Checkbox:
        return LightCheckbox(label)
    
    def create_label(self, text: str) -> Label:
        return LightLabel(text)
