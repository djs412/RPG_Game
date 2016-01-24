##Zones

class Zone:

    def __init__(self, name = None, next = None):
        self.name = name
        self.monsterlist = []
        self.merchants = []
        self.next = next

    def __str__(self):
        return self.name

class Forest(Zone):

    monsterlist = [Goblin, Rat, Ogre, Skeleton]

    
