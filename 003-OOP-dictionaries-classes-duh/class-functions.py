class Character():
    def __init__(self, name, c_class, level, inventory):
        self.name = name
        self.c_class = c_class
        self.level = level
        self.inventory = inventory

    def add_item(self, item):
        self.inventory.append(item)

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            print(f'{self.name} does not have item: {item}')

new_character = Character("Bartholomew", "Paladin", "13", ["Longsword", "Shield", "Rations", "Map", "Rosary", "Waterskin"])
while True:
    try:
        operation = int(input(
            f'1: Add item to inventory. \n2: Remove item from inventory. \n3: Exit program. \n Option: '))

        if operation == 1:
            new_item = input(f"What item do you want to add to {new_character.name}? \n New item: ")
            new_character.add_item(new_item)
            print(new_character.inventory)
        elif operation == 2:
            old_item = input(f"What item do you want to remove from {new_character.name}? \n Item: ")
            new_character.remove_item(old_item)
            print(new_character.inventory)
        elif operation == 3:
            exit()
    except ValueError:
        print("Use a integer please.")


    