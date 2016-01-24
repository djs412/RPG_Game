##Backpack

from Items import *

class Pocket:
    ##This is a node for the linked list class:Backpack

    def __init__(self, cargo = None, next = None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)

class Backpack:
    ##This is a linked list, made up of Pockets (nodes)

    def __init__(self):
        self.head = None
        self.length = 0

    def __str__(self):
        return str(self.head)

    def add_first(self, cargo):
        node = Pocket(cargo)
        node.next = self.head
        self.head = node
        self.length += 1

    def remove_first(self, cargo):
        """Takes str argument"""
        node = self.head
        previous = self.head
        while node is not None:
            if str(node.cargo) == cargo and node == self.head:
                self.head = node.next
                return node
            if str(node.cargo) == cargo:
                previous.next = node.next
                return node
            previous = node
            node = node.next
        return "nothing"
            

    def print_list(self):
        node = self.head
        count = 1
        print("Backpack contents: ")
        while node is not None:
            print(count, end = ": ")
            print(node)
            count += 1
            node = node.next

    def print_nicely(self):
        print("[ ", end = "")
        self.print_list()
        print("]")

item1 = Broadsword()
item2 = Chainmail()

pack = Backpack()
pack.add_first(item1)
pack.add_first(item2)
pack.add_first(Mace())
pack.add_first(Broadsword())


print(pack.remove_first("Chainmail"))
pack.print_list()
