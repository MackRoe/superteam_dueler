import random

""" code under construction """


class Ability:
    def __init__(self, name, attack_strength):
        # instance variables
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        # print(self.name + " attacks!")  -- outside of specs --
        attack_now = random.randint(0, self.max_damage)
        # creates a randomly rated attack
        return attack_now


class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max.block

    def block(self):
        block_now = random.randint(0, max_block)
        # creates a randomly rated blocking action
        return block_now 


class Hero:
    def __init__(self, name, starting_health=100):
        # Initialize instance variables values as instance variables
        damage = 0
        # set starting value for damage
        self.abilities = []
        self.armors = []
        # abilities and armors are lists that will contain objects
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health - damage
        
        pass


if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    """ test code from tutorial """
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())
    my_hero = Hero("Auntie M", 200)
    print(my_hero.name)
    print(my_hero.current_health)