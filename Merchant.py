##Shop
from Items import *
from helpers import *

class Merchant:

    def __init__(self):
        self.name = "Charles"
        self.inventory = [Broadsword(), Chainmail(), Mace()]

    def __str__(self):
        return str(self.name)

    def print_inventory(self):
        for index, item in enumerate(self.inventory[:len(self.inventory)-1]):
            print(index, ": ", end = "")
            slow_print([item.name], .02)
        print(index + 1, ": ", end = "")
        slow_print([self.inventory[-1].name], .02)

    def sell(self, target):
        slow_print(["Hello there! My name is {0}!".format(
                    self.name)], .02)
        deci = input("Would you like to look at my wares?")
        print()
        if helper(deci) == "y":
            self.print_inventory()
            purchase = input("What would you like to purchase?")
            """Enter the number of the item listing"""
            print()
            a = target.purchase(self.inventory[int(purchase)])
            print()
            if a == 1:
                eq = helper(input("Would you like to equip it now?"))
                if eq == "y":
                    
                    if self.inventory[int(purchase)].itemtype == "Weapon":
                        if target.equipped_weapon != "":
##                            target.unequip(target.equipped_weapon)
                            
                            target.unequip_weapon()
                            target.equip(self.inventory[int(purchase)])
                        target.equip(self.inventory[int(purchase)])
                    else:
                        if target.equipped_armor != "":
                            target.unequip(target.equipped_armor)
                        target.equip(self.inventory[int(purchase)])
        print()
        


class AbrahamLincoln(Merchant):

    def __init__(self):
        self.name = "Abraham Lincoln"
        self.inventory = [UltimateWeapon(), UltimateArmor()]

class Donald(Merchant):

    def __init__(self):
        self.name = "Donald"
        self.inventory = [LeatherArmor(), Chainmail(), Mace(), Broadsword()]

merchantlist = [AbrahamLincoln, Donald]


