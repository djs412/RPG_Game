##Player
import random
from Items import *
from helpers import *
from Backpack import *

class player:

    def __init__(self, name):
        self.hp = 100
        self.maxhp = 100
        self.mp = 10
        self.maxmp = 10
        
        self.stam = 30
        self.maxstam = 30
        self.exp = 0
        self.level = 1
        self.name = name
        self.inven = {"health_pot": 3}
        self.backpack = []
        self.gold = 1
        self.weapon = True
        self.equipped_weapon = Mace()
        self.atk = 20 
        self.armor = True
        self.equipped_armor = LeatherArmor()
        self.defense = 0 
        self.pack = Backpack()
        

    def __str__(self):
        return """
Name: {0}
HP: {1}
MP: {2}
ATK: {3}
STAM: {4}
EXP: {5}
INV: {6}
GOLD: {7}
MAX HP: {8}
MAX MP: {9}
ARMOR: {10}
LEVEL: {11}
""".format(self.name, self.hp, self.mp,
           self.atk, self.stam, self.exp,
           self.inven, self.gold, self.maxhp,
           self.maxmp, self.defense, self.level)

    def rest(self):
        
        p.hp = p.maxhp
        p.mp = p.maxmp
        p.stam = p.maxstam
        slow_print(["You recover all your health and stamina"], .02)
        p.level_up()


    def attack(self, target):
        rng = random.Random()
        dmg = rng.randrange(self.atk/2, self.atk) - target.defense + self.equipped_weapon.atk_value
        target.hp -= dmg
        print("You attack the {0} for {1} points of damage".format(
            target.name, dmg))
        
        if target.defense >0:
            print()
            print("The {0}'s armor prevents {1} point(s) of damage.".format(
                target.name, target.defense))
        print()

    def heavy_attack(self, target):
        if self.stam >= 5:
            rng = random.Random()
            dmg = rng.randrange(self.atk, self.atk*2) - target.defense + self.equipped_weapon.atk_value
            self.stam -= 5
            target.hp -= dmg
            print("You attack the {0} heavily for {1} points of damage".format(
                target.name, dmg))
            if target.defense >0:
                print()
                print("The {0}'s armor prevents {1} point(s) of damage.".format(
                    target.name, target.defense))
            print()
        else:
            print("You are exhausted!")
            print()

    def drink_pot(self):
        if self.inven["health_pot"] >= 1:
            self.inven["health_pot"] -= 1
            self.hp += 50
            print("You drink a potion and recover 50 health")
            print()
        else:
            print("You don't have any potions remaining")
            print()

    def level_up(self):
        if self.exp >= 10 + 5*self.level:
            self.exp -= (10+5*self.level)
            self.level += 1
            self.maxhp += (25+5*self.level)
            self.hp = self.maxhp
            self.maxmp += (2 + 2*self.level)
            self.mp = self.maxmp
            self.atk += 2 + 2*self.level
            print("""You level up and gain {0} attack,
                  {1} hp and {2} mp!""".format((2+2*self.level),
                                          (2+2*self.level), (2+2*self.level)))
            print()
            

    def purchase(self, item):
        if self.gold >= item.value:
            self.backpack.append(item)
            self.gold -= item.value
            slow_print(["You have purchased the {0} for {1} gold!".format(
                item.name, item.value)], .01)
            self.pack.add_first(item)
            return 1
        print("You do not have enough gold")

    def equip(self, item):
        if item.itemtype == "Weapon" and self.weapon == False:          
            self.equipped_weapon = item
            self.weapon = True
            print("You equip your {0}".format(item.name))
            self.pack.remove_first(str(item))
        if item.itemtype == "Armor" and self.armor == False:          
            self.equipped_armor = item
            self.armor = True
            print("You equip your {0}".format(item.name))
            self.pack.remove_first(str(item))

##    def unequip(self, item):
##        
##        if item.itemtype == "Weapon" and self.weapon == True:
##            self.weapon = False
##            self.equipped_weapon = ""
##            print("You unequip your {0}".format(item.name))
##        if item.itemtype == "Armor" and self.armor == True:
##            self.equipped_armor = ""
##            self.armor = False
##            print("You unequip your {0}".format(item.name))

    def unequip_armor(self):
        if self.equipped_armor != "":
            self.pack.add_first(self.equipped_armor)
        self.equipped_armor = LeatherArmor()
        self.armor = False

    def unequip_weapon(self):
        if self.equipped_weapon != "":
            self.pack.add_first(self.equipped_weapon)
        self.equipped_weapon = Mace()
        self.weapon = False

