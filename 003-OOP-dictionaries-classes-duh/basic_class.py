class Character():
    def __init__(self, name, c_class, level, inventory):
        self.name = name
        self.c_class = c_class
        self.level = level
        self.inventory = inventory

new_character = Character("Bartholomew", "Paladin", "13", ["Longsword", "Shield", "Rations", "Map", "Rosary", "Waterskin"])
print(new_character.level)