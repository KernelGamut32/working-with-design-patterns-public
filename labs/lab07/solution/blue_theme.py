from products import Button, TextField, Checkbox, Label
from factories import GUIFactory

class BlueButton(Button):
    def __init__(self, caption: str):
        self.caption = caption

    def render(self) -> None:
        print(f"[Blue Button] [ {self.caption} ] rendered with blue background, white text.")

    def on_click(self) -> None:
        print(f"[Blue Button] '{self.caption}' was clicked. (Blue theme style)")

class BlueTextField(TextField):
    def __init__(self, placeholder: str):
        self.placeholder = placeholder
        self.text = ""

    def render(self) -> None:
        print(f"[Blue TextField] <{self.placeholder}> rendered with blue background, white border.")

    def get_input(self) -> str:
        self.text = f"UserInput_for_{self.placeholder}"
        print(f"[Blue TextField] Received input: '{self.text}'")
        return self.text

class BlueCheckbox(Checkbox):
    def __init__(self, label: str):
        self.label = label
        self.checked = False

    def render(self) -> None:
        state = "✔" if self.checked else " "
        print(f"[Blue Checkbox] [ {state} ] {self.label} (blue background)")

    def toggle(self) -> bool:
        self.checked = not self.checked
        print(f"[Blue Checkbox] '{self.label}' toggled to {'checked' if self.checked else 'unchecked'}.")
        return self.checked

class BlueLabel(Label):
    def __init__(self, text: str):
        self.text = text

    def render(self) -> None:
        print(f"[Blue Label] {self.text} (blue background)")

class BlueThemeFactory(GUIFactory):
    def create_button(self, caption: str) -> Button:
        return BlueButton(caption)

    def create_textfield(self, placeholder: str) -> TextField:
        return BlueTextField(placeholder)

    def create_checkbox(self, label: str) -> Checkbox:
        return BlueCheckbox(label)
        
    def create_label(self, text: str) -> Label:
        return BlueLabel(text)
