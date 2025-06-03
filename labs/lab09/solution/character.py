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
        level: int = 1,
        equipment: list[Equipment] = None,
        skills: list[str] = None
    ):
        self.name = name
        self.char_type = char_type
        self.health = health
        self.mana = mana
        self.level = level
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
    
    def customize_clone(
            self,
            new_name: str,
            extra_equipment: Equipment = None,
            extra_skill: str = None
    ) -> "GameCharacter":
        clone_character = self.clone()
        clone_character.name = new_name

        if extra_equipment:
            clone_character.add_equipment(extra_equipment)
        if extra_skill:
            clone_character.add_skill(extra_skill)

        return clone_character

    def __str__(self) -> str:
        eq_str = ", ".join(str(e) for e in self.equipment) or "None"
        skills_str = ", ".join(self.skills) or "None"
        return (
            f"Name: {self.name}\n"
            f" Type: {self.char_type}\n"
            f" Health: {self.health} | Mana: {self.mana}\n"
            f" Level: {self.level}\n"
            f" Equipment: {eq_str}\n"
            f" Skills: {skills_str}"
        )

    def __repr__(self) -> str:
        return (
            f"GameCharacter(name={self.name!r}, char_type={self.char_type!r}, "
            f"health={self.health!r}, mana={self.mana!r}, "
            f"equipment={self.equipment!r}, skills={self.skills!r})"
        )
    