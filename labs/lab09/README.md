# Lab 09 - Prototype and Builder Patterns

## Overview

In this lab, you’ll work hands-on with a Python application that demonstrates two creational design patterns:

1. **Builder Pattern:** Assemble complex `GameCharacter` objects step-by-step, using a `CharacterBuilder` (and an optional `CharacterDirector` for presets).
2. **Prototype Pattern:** Clone existing `GameCharacter` instances via deep copy, then modify the clones without affecting the originals.

By the end of this lab, you will:

- Understand how the Builder pattern separates object construction from representation.
- Use a `CharacterBuilder` (and `CharacterDirector`) to create different “archetype” characters.
- Observe how the Prototype pattern enables you to clone objects and modify clones safely.
- Extend and modify the provided code to enforce deeper mastery of both patterns.

---

## Prerequisites

Before you begin, ensure the following:

1. Python 3.8+ installed - Confirm by running `python --version` in your terminal.
2. An editor or IDE capable of editing multiple `.py` files (e.g., VS Code, PyCharm, Sublime Text).
3. Familiarity with basic OOP in Python - You should know what classes, methods, and imports/modules are.
4. Basic comfort with the command line - You’ll navigate directories and launch Python scripts.

---

## File Structure

Create a new folder on your local machine (e.g., `design_patterns_lab/`). Inside that folder, create four files exactly as named below:

```text
design_patterns_lab/
├── equipment.py
├── character.py
├── builder.py
└── main.py
```

- **equipment.py:** Defines an `Equipment` class that each character can hold.
- **character.py:** Defines the `GameCharacter` class, including a `clone()` method (Prototype).
- **builder.py:** Defines `CharacterBuilder` and `CharacterDirector` (Builder).
- **main.py:** A driver script that builds characters, clones them, and prints results.

---

## Examine the Code

equipment.py

```python
class Equipment:
    """
    Represents a piece of equipment (weapon, armor, etc.) that a character can own.
    """
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power

    def __str__(self) -> str:
        return f"{self.name} (Power: {self.power})"

    def __repr__(self) -> str:
        return f"Equipment(name={self.name!r}, power={self.power!r})"
```

character.py

```python
import copy
from equipment import Equipment

class GameCharacter:
    """
    A game character with various attributes, equipment, and skills.
    Implements a `clone()` method to create deep copies (Prototype pattern).
    """
    def __init__(
        self,
        name: str,
        char_type: str,
        health: int,
        mana: int,
        equipment: list[Equipment] = None,
        skills: list[str] = None
    ):
        self.name = name
        self.char_type = char_type
        self.health = health
        self.mana = mana
        # Use slicing to avoid aliasing incoming lists
        self.equipment = equipment[:] if equipment else []
        self.skills = skills[:] if skills else []

    def add_equipment(self, equip: Equipment) -> None:
        """
        Add one Equipment object to this character.
        """
        self.equipment.append(equip)

    def add_skill(self, skill: str) -> None:
        """
        Add one skill (by name) to this character.
        """
        self.skills.append(skill)

    def clone(self) -> "GameCharacter":
        """
        Create a deep copy of this character (Prototype pattern).
        """
        return copy.deepcopy(self)

    def __str__(self) -> str:
        eq_str = ", ".join(str(e) for e in self.equipment) or "None"
        skills_str = ", ".join(self.skills) or "None"
        return (
            f"Name: {self.name}\n"
            f" Type: {self.char_type}\n"
            f" Health: {self.health} | Mana: {self.mana}\n"
            f" Equipment: {eq_str}\n"
            f" Skills: {skills_str}"
        )

    def __repr__(self) -> str:
        return (
            f"GameCharacter(name={self.name!r}, char_type={self.char_type!r}, "
            f"health={self.health!r}, mana={self.mana!r}, "
            f"equipment={self.equipment!r}, skills={self.skills!r})"
        )
```

builder.py

```python
from character import GameCharacter
from equipment import Equipment

class CharacterBuilder:
    """
    Builder for assembling a GameCharacter step by step.
    After `build()` is called, the builder resets its internal state.
    """
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        """
        Reset all internal fields so you can build a fresh character.
        """
        self._name: str = ""
        self._char_type: str = ""
        self._health: int = 0
        self._mana: int = 0
        self._equipment: list[Equipment] = []
        self._skills: list[str] = []

    def set_name(self, name: str) -> "CharacterBuilder":
        self._name = name
        return self

    def set_type(self, char_type: str) -> "CharacterBuilder":
        self._char_type = char_type
        return self

    def set_health(self, health: int) -> "CharacterBuilder":
        self._health = health
        return self

    def set_mana(self, mana: int) -> "CharacterBuilder":
        self._mana = mana
        return self

    def add_equipment(self, equipment: Equipment) -> "CharacterBuilder":
        self._equipment.append(equipment)
        return self

    def add_skill(self, skill: str) -> "CharacterBuilder":
        self._skills.append(skill)
        return self

    def build(self) -> GameCharacter:
        """
        Constructs a GameCharacter from current state, then resets to allow building another.
        """
        character = GameCharacter(
            name=self._name,
            char_type=self._char_type,
            health=self._health,
            mana=self._mana,
            equipment=self._equipment,
            skills=self._skills
        )
        self.reset()
        return character


class CharacterDirector:
    """
    Director that provides “recipes” (presets) for common character types.
    It uses a CharacterBuilder internally to streamline construction.
    """
    def __init__(self, builder: CharacterBuilder):
        self._builder = builder

    def build_warrior(self, name: str) -> GameCharacter:
        """
        Creates a standard Warrior: high health, some mana, sword + shield, two basic skills.
        """
        return (
            self._builder
            .set_name(name)
            .set_type("Warrior")
            .set_health(150)
            .set_mana(30)
            .add_equipment(Equipment("Sword", 12))
            .add_equipment(Equipment("Shield", 8))
            .add_skill("Slash")
            .add_skill("Block")
            .build()
        )

    def build_mage(self, name: str) -> GameCharacter:
        """
        Creates a standard Mage: lower health, high mana, staff + robe, two magic skills.
        """
        return (
            self._builder
            .set_name(name)
            .set_type("Mage")
            .set_health(80)
            .set_mana(150)
            .add_equipment(Equipment("Staff", 10))
            .add_equipment(Equipment("Robe", 4))
            .add_skill("Fireball")
            .add_skill("Teleport")
            .build()
        )

    def build_archer(self, name: str) -> GameCharacter:
        """
        Creates a standard Archer: balanced health/mana, bow + light armor, two ranged skills.
        """
        return (
            self._builder
            .set_name(name)
            .set_type("Archer")
            .set_health(120)
            .set_mana(60)
            .add_equipment(Equipment("Bow", 11))
            .add_equipment(Equipment("Leather Armor", 5))
            .add_skill("Piercing Arrow")
            .add_skill("Eagle Eye")
            .build()
        )
```

main.py

```python
from builder import CharacterBuilder, CharacterDirector
from character import GameCharacter
from equipment import Equipment


def main():
    # 1) Use Builder directly to craft a custom "Rogue"
    builder = CharacterBuilder()
    rogue = (
        builder
        .set_name("Shade")
        .set_type("Rogue")
        .set_health(100)
        .set_mana(70)
        .add_equipment(Equipment("Dagger", 9))
        .add_equipment(Equipment("Leather Armor", 6))
        .add_skill("Stealth")
        .add_skill("Backstab")
        .build()
    )

    print("=== Custom Rogue Character (built via Builder) ===")
    print(rogue)
    print()

    # 2) Use Director to build standard characters
    director = CharacterDirector(CharacterBuilder())

    warrior = director.build_warrior("Thorin")
    mage = director.build_mage("Gandalf")
    archer = director.build_archer("Legolas")

    print("=== Warrior (Director) ===")
    print(warrior)
    print()

    print("=== Mage (Director) ===")
    print(mage)
    print()

    print("=== Archer (Director) ===")
    print(archer)
    print()

    # 3) Demonstrate Prototype: clone an existing character
    print("=== Demonstrating Prototype (cloning) ===")
    warrior_clone: GameCharacter = warrior.clone()
    warrior_clone.name = "Thorin the Brave"
    warrior_clone.add_skill("War Cry")

    print("-- Original Warrior --")
    print(warrior)
    print()

    print("-- Cloned & Modified Warrior --")
    print(warrior_clone)
    print()

    # 4) Show that modifying the clone’s equipment or skills does NOT affect the original
    warrior_clone.add_equipment(Equipment("Battle Axe", 15))
    print("After adding 'Battle Axe' to the clone’s equipment:")
    print("-- Original Warrior still has: --")
    print(warrior)
    print()
    print("-- Clone’s equipment now: --")
    print(warrior_clone)
    print()


if __name__ == "__main__":
    main()
```

To execute/test, run `python main.py`

---

## Additional Exercises (Time Permitting)

### Exercise 1: Add a New "Level" attribute

Each `GameCharacter` should have a new attribute called `level` (an integer value) in addition to `health` and `mana`, defaulted to 1 if not provided. Update the `__str__` method so it prints "Level: X" on its own line alongside the other output.

### Exercise 2: Create a "Paladin" preset in `CharacterDirector`

Paladin has moderate health/mana, a "Holy Sword", "Plate Armor", and skills "Smite" and "Heal". Default level = 3.

### Exercise 3: Implement a `customize_clone` Method

In `character.py`, write a new method called `customize_clone(new_name: str, extra_equipment: Equipment = None, extra_skill: str = None)`. This method should:

- Clone `self`.
- Set the clone's `name` to `new_name`.
- If `extra_equipment` is provided, add to the clone.
- If `extra_skill` is provided, add to the clone.
- Return the modified clone.

In `main.py`, test the `customize_clone` method.

### Exercise 4: Allow Equipment to be Upgradeable

Modify `Equipment` so that it has a `level` attribute (int) with a default value of 1. Implement an
`upgrade()` method that increases `power` by 20% and increments `level` by 1. Test it out on one of
your characters in `main.py` - upgrade a piece of equipment for one of your characters and verify the
results via console output.
