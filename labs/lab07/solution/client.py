from products import Button, TextField, Checkbox, Label
from factories import GUIFactory

class LoginForm:
    def __init__(self, factory: GUIFactory):
        self.username_label: Label = factory.create_label("Username:")
        self.username_field: TextField = factory.create_textfield("Username")
        self.password_label: Label = factory.create_label("Password:")
        self.password_field: TextField = factory.create_textfield("Password")
        self.remember_me_checkbox: Checkbox = factory.create_checkbox("Remember Me")
        self.submit_button: Button = factory.create_button("Submit")

    def render(self) -> None:
        print("---- Rendering Login Form ----")
        self.username_label.render()
        self.username_field.render()
        self.password_label.render()
        self.password_field.render()
        self.remember_me_checkbox.render()
        self.submit_button.render()
        print("--------------------------------\n")

    def simulate_interaction(self) -> None:
        print("---- Simulating user interaction ----")
        username_value = self.username_field.get_input()
        password_value = self.password_field.get_input()
        remember_state = self.remember_me_checkbox.toggle()

        print(f"Collected credentials: username='{username_value}', password='{password_value}'.")
        print(f"Remember Me checked? {'Yes' if remember_state else 'No'}.\n")

        self.submit_button.on_click()
        print("---- Interaction complete ----")
