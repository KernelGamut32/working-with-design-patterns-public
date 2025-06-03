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
        self._level: int = 1
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
    
    def set_level(self, level: int) -> "CharacterBuilder":
        self._level = level
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
            level=self._level,
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
            .set_level(4)
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
    
    def build_paladin(self, name: str) -> GameCharacter:
        """
        Creates a standard Paladin: moderate health, moderate mana, sword + armor, smite + healing skills, default level of 3.
        """
        return (
            self._builder
            .set_name(name)
            .set_type("Paladin")
            .set_health(140)
            .set_mana(80)
            .set_level(3)
            .add_equipment(Equipment("Holy Sword", 14))
            .add_equipment(Equipment("Plate Armor", 10))
            .add_skill("Smite")
            .add_skill("Heal")
            .build()
        )
