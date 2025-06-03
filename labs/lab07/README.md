# Lab 07 - Factory/Abstract Factory Pattern

## Overview

In this lab, you will explore the **Abstract Factory** design pattern by working with a small Python application that simulates a themable UI toolkit. The application defines abstract interfaces for UI components (buttons, text fields, checkboxes) and two “theme” variants (Light and Dark). You will:  

1. Run and observe how the same client code produces different output based on the selected theme.  
2. Examine each module to understand how abstract products and factories are defined.  
3. Extend the existing code by adding a new theme or a new product type.  

By the end of this lab, you should be able to:  

- Explain how the Abstract Factory pattern decouples client code from concrete implementations.  
- Identify the roles of abstract products, concrete products, abstract factory, and concrete factories.  
- Modify and extend an Abstract Factory–based codebase without changing the client logic.

---

## Learning Objectives

- Recognize when and why to use the Abstract Factory pattern.  
- Understand how multiple related families of objects can be created without coupling client code to their concrete classes.  
- Implement abstract product interfaces and concrete variants in Python.  
- Use Python’s `abc` module to define abstract base classes (ABCs) that enforce method signatures.  
- Extend the pattern by adding new concrete factories and products.

---

## Prerequisites

Before starting, students should already be comfortable with:  

- Basic Python programming (functions, classes, modules, imports).  
- Object-oriented concepts such as inheritance and polymorphism.  
- The `abc` module in Python (`@abstractmethod`).  
- Running a Python script from the command line.

---

## Repository Structure

Place the following six files in a directory named `abstract_factory_app/`:

```text
abstract_factory_app/
├── products.py
├── factories.py
├── light_theme.py
├── dark_theme.py
├── client.py
└── main.py
```

Below is a brief summary of each file’s purpose:

1. **products.py**: Defines the abstract product interfaces: `Button`, `TextField`, `Checkbox`.  
2. **factories.py**: Defines the abstract factory interface (`GUIFactory`) and a helper function (`get_factory`) that returns a concrete factory based on a theme name.  
3. **light_theme.py**: Implements concrete products for the Light theme (`LightButton`, `LightTextField`, `LightCheckbox`) and the `LightThemeFactory` that bundles them.  
4. **dark_theme.py**: Implements concrete products for the Dark theme (`DarkButton`, `DarkTextField`, `DarkCheckbox`) and the `DarkThemeFactory`.  
5. **client.py**: Contains the client code (`LoginForm`), which uses only abstract interfaces (`Button`, `TextField`, `Checkbox`, and `GUIFactory`). The client builds and renders a login form, then simulates user interaction.  
6. **main.py**: Entry point. Reads the command-line argument (`light` or `dark`), obtains the appropriate concrete factory, instantiates `LoginForm`, calls its `render()` and `simulate_interaction()` methods, and prints output.

---

## Examine the Code

products.py

```python
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
```

**Key point:** The client will depend on these abstract interfaces onlly.

factories.py

```python
from abc import ABC, abstractmethod
from products import Button, TextField, Checkbox

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

def get_factory(theme: str) -> GUIFactory:
    theme = theme.strip().lower()
    if theme == "light":
        from light_theme import LightThemeFactory
        return LightThemeFactory()
    elif theme == "dark":
        from dark_theme import DarkThemeFactory
        return DarkThemeFactory()
    else:
        raise ValueError(f"Unsupported theme '{theme}'.")
```

**Key point:** `GUIFactory` is the abstract factory. It declares methods to create each type of product. The helper `get_factory()` returns a concrete factory based on the theme string.

light_theme.py

```python
from products import Button, TextField, Checkbox
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

class LightThemeFactory(GUIFactory):
    def create_button(self, caption: str) -> Button:
        return LightButton(caption)

    def create_textfield(self, placeholder: str) -> TextField:
        return LightTextField(placeholder)

    def create_checkbox(self, label: str) -> Checkbox:
        return LightCheckbox(label)
```

**Key point:** Each concrete product implements its respective abstract interface. The factory methods return instances of these concrete classes.

dark_theme.py - It mirrors `light_theme.py`, but with "Dark" prefixes and different text in each `render()` call.

```python
from products import Button, TextField, Checkbox
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

class DarkThemeFactory(GUIFactory):
    def create_button(self, caption: str) -> Button:
        return DarkButton(caption)

    def create_textfield(self, placeholder: str) -> TextField:
        return DarkTextField(placeholder)

    def create_checkbox(self, label: str) -> Checkbox:
        return DarkCheckbox(label)
```

**Key point:** Changing only these classes (and not client code) switches the “look and feel.”

client.py

```python
from products import Button, TextField, Checkbox
from factories import GUIFactory

class LoginForm:
    def __init__(self, factory: GUIFactory):
        self.username_field: TextField = factory.create_textfield("Username")
        self.password_field: TextField = factory.create_textfield("Password")
        self.remember_me_checkbox: Checkbox = factory.create_checkbox("Remember Me")
        self.submit_button: Button = factory.create_button("Submit")

    def render(self) -> None:
        print("---- Rendering Login Form ----")
        self.username_field.render()
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
```

**Key point:** `LoginForm` is completely unaware of “Light” or “Dark.” It calls only the abstract methods.

main.py

```python
import sys
from factories import get_factory
from client import LoginForm

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <theme>")
        print("Available themes: 'light', 'dark'")
        sys.exit(1)

    theme = sys.argv[1]
    try:
        factory = get_factory(theme)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    form = LoginForm(factory)
    form.render()
    form.simulate_interaction()

if __name__ == "__main__":
    main()
```

**Key point:** This is where you choose which concrete factory to inject into the client.

To execute/test, run `python main.py <theme>`.

---

## Additional Exercises (Time Permitting)

### Exercise 1: Add a "Blue" Theme

### Exercise 2: Add an Additional Product Type (“Label”)

Suppose you want every form to show a static text label (e.g., “Username:” and “Password:”) before each text field. That requires a new product interface, new concrete implementations, and changes in client code.
