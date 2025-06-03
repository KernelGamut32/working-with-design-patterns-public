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
    paladin = director.build_paladin("Arthas")

    print("=== Warrior (Director) ===")
    print(warrior)
    print()

    print("=== Mage (Director) ===")
    print(mage)
    print()

    print("=== Archer (Director) ===")
    print(archer)
    print()

    print("=== Paladin (Director) ===")
    print(paladin)
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

    customized = paladin.customize_clone(
        new_name="Uther the Lightbringer",
        extra_equipment=Equipment("War Hammer", 20),
        extra_skill="Shield Bash"
    )
    print("-- Original Paladin --")
    print(paladin)
    print()
    print("-- Customized Clone --")
    print(customized)
    print()

    first_equipment = archer.equipment[0]
    print("-- Archer's first equipment before upgrade --")
    print(f"    {first_equipment}")

    first_equipment.upgrade()

    print("-- Archer's first equipment after upgrade --")
    print(f"    {first_equipment}")


if __name__ == "__main__":
    main()
