class Equipment:
    """
    Represents a piece of equipment (weapon, armor, etc.) that a character can own.
    """
    def __init__(self, name: str, power: int):
        self.name = name
        self.power = power
        self.level = 1

    def upgrade(self) -> None:
        """
        Upgrade the equipment by increasing its power by 20%.
        """
        new_power = round(self.power * 1.2)
        self.power = new_power
        self.level += 1

    def __str__(self) -> str:
        return f"{self.name} (Power: {self.power}, Level: {self.level})"

    def __repr__(self) -> str:
        return f"Equipment(name={self.name!r}, power={self.power!r})"
    