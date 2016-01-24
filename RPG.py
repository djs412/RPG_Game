##RPG game

from PlayerClass2 import player
from helpers import *
import time
import random


d = player("Dave")
g = player("Goblin")

def encounter(player, monster):
    rng = random.Random()
    print("You encounter a wild {0}!".format(monster.name))
    print()
    time.sleep(0.75)
    while True:
        if player.hp <= 0:
            slow_print(["You died"], 0.2)
            for i in range(3):
                time.sleep(1)
                print()
            break
        if monster.hp <= 0:
            print("""You defeat the {0} and gain {1} gold and {2} experience
                  """.format(monster.name, monster.gold, monster.exp))
            player.exp += monster.exp
            player.gold += monster.gold
            print()
            time.sleep(1)
            break
        
        decision = helper(input("Will you (a)ttack, (h)eavy attack, (d)rink potion, or (r)un away?"))
        print()

        if decision == "a":
            player.attack(monster)
        if decision == "h":
            player.heavy_attack(monster)
        if decision == "d":
            player.drink_pot()
        if decision == "r":
            getaway = rng.choice(range(3))
            print(getaway)
            if getaway == 1:
                print("""You run away successfully. If you want to consider running away
a success, that is""")
                break
            else:
                print("""You fail to run away""")

        mon_decision = rng.randrange(0, 100)
        
        if mon_decision <= 70:
            monster.attack(player)
        if 71 <= mon_decision <= 90:
            monster.critical(player)
        if 91 <= mon_decision:
            if monster.inven["health_pot"] >= 1:
                monster.drink_pot()
            else:
                monster.attack(player)
        




    
