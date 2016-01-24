##Game

from textdump import *
from helpers import *
from PlayerClass2 import *
from Monster import *
from RPG import *
from Items import *
from Merchant import *
from Backpack import *


def camp(p):
    rng = random.Random()
    first_time = True
    p.gold = 10
    while True:
        if p.hp <= 0:
            slow_print(["""Let us go out this evening for pleasure.""",
    """          The night is still young."""], .08)
            break
        options = ["1. (B)attle Monsters", "2. (R)est",
                                    "3. (A)rmor Upgrade", "4. (W)eapon Upgrade",
                                    "5. (C)heck status", "6. (I)nspect Backpack",
                                    "7. (S)hop", "8. (Q)uit"]
        if first_time != True:
            for i in options:
                print(i)
            print()
        if first_time == True:
            slow_print(options, 0.02)
            first_time = False
        
        dec = helper(input("What will you do?"))
        print()
        if dec == "q":
            break
        if dec == "r":
            rest = input(
                "Would you like to rest at the inn for 1 gold?",
                                   )
            if helper(rest) == "y":
                if p.gold >= 1:
                    p.gold -= 1
                    p.rest()
                else:
                    print()
                    slow_print(["You do not have enough gold.",
                                "Get a job, you filthy hippie"], .02)
            if helper(rest) == "n":
                print()
                slow_print(["Fine, we don't want your business anyway, freak"],
                           .02)
        if dec == "b":
            counter = 0
            while counter <= 30:
                mon = rng.choice(monsterlist)
                mon = mon()
                
                if abs(p.level - mon.level) <= 2:
                    encounter(p, mon)
                    break
                counter += 1
##                for i in range(3):
##                    time.sleep(.8)
##                    print(".", end = " ")
##                time.sleep(.8)
##                if p.hp >0:
##                    print()
##                    slow_print(["There are no monsters around."], .02)
##                    print()
##                continue
        if dec == "c":
            print(p)
        if dec == "a":
            armor_decision = input(
                "Do you want to upgrade your armor for 5 gold?")
            if p.equipped_armor == "":
                slow_print(["You do not have armor equipped"], .02)
                continue
            if helper(armor_decision) == "y" and p.gold >= 5:
                p.equipped_armor.armor_value += 3
                val = p.equipped_armor.armor_value
                p.gold -= 5
                print("Your {0}'s Armor Value has increased from {1} to {2}!".format(
                    p.equipped_armor, val - 3, val))
            if p.gold < 5:
                print("You do not have enough gold")
        if dec == "w":
            weapon_decision = input(
                "Do you want to upgrade your weapon for 5 gold?")
            if p.equipped_weapon == "":
                slow_print(["You do not have a weapon equipped"], .02)
                continue
            if helper(weapon_decision) == "y" and p.gold >= 5:
                p.equipped_weapon.atk_value += 3
                val = p.equipped_weapon.atk_value
                p.gold -= 5
                print("Your {0}'s Attack Value has increased from {1} to {2}!".format(
                    p.equipped_weapon, val - 3, val))
            if p.gold < 5:
                print("You do not have enough gold")
        if dec == "s":
            merch = rng.choice(merchantlist)
            merch = merch()
            merch.sell(p)
        if dec == "i":
            p.pack.print_list()
            x = input("Press enter to continue")
            
       
                
camp(player("Dave"))

##p = player("Dave")
##g = Broadsword()
##h = Chainmail()
##p.equip(g)
##print(p.atk)
##p.unequip_weapon()
##p.equip(Mace())
##print(p.atk)
##print(p.pack)
##p.equip(h)
##p.unequip_armor()
##print(p.equipped_armor())
