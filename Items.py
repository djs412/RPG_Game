##Items, Weapons, Armor

class Item:

    def __init__(self, item_name):
        self.name = item_name

    def __str__(self):
        return str(self.name)

            
class Armor(Item):
    itemtype = "Armor"

    def __init__(self):
        self.armor_value = 0

    

class LeatherArmor(Armor):

    def __init__(self):
        self.armor_value = 5
        self.armor_value_max = 15
        self.value = 3
        self.name = "Leather Armor"

class Chainmail(Armor):
    
    def __init__(self):
        self.armor_value = 10
        self.armor_value_max = 25
        self.value = 10
        self.name = "Chainmail"

class UltimateArmor(Armor):

    def __init__(self):
        self.armor_value = 100
        self.armor_value_max = 500
        self.value = 200
        self.name = "Ultimate Impenetrable Armor of Long-lost Mysteries"

class Weapon(Item):
    itemtype = "Weapon"

    def __init__(self):
        self.atk_value = 0

    def __ty__(self):
        return ty
        
class Broadsword(Weapon):

    def __init__(self):
        self.atk_value = 5
        self.atk_value_max = 15
        self.value = 3
        self.name = "Broadsword"

class Mace(Weapon):

    def __init__(self):
        self.atk_value = 3
        self.atk_value_max = 9
        self.value = 2
        self.name = "Mace"

class UltimateWeapon(Weapon):

    def __init__(self):
        self.atk_value = 200
        self.atk_value_max = 500
        self.value = 250
        self.name = "Ultimate Weapon of Ancient Forgotten Secrets"

    
