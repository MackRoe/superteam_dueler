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
        abilities = []
        armors = []
        # set starting values
        self.abilities = abilities
        self.armors = armors
        # abilities and armors are lists that will contain objects
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health - damage


    def add_ability(self, ability):
        self.abilities.append(ability)
        """ Add ability to abilities list """
        # return abilities

    
    def attack(self, name, attack_strength):
        for each in range(abilities):
            total_damage = damage + Ability.attack()
            return total_damage

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    """ test code from tutorial """
    ability = Ability("Debugging Ability", 20)
    print("Ability Name: " + ability.name)
    print("Ability Strength: " + str(ability.attack()))
    ability = Ability("Smite", 25)
    hero = Hero("Auntie M", 200)
    print("Hero Name: " + hero.name)
    print("Current Health: " + str(hero.current_health))
    hero.add_ability("Force Wave")
    hero.add_ability("Lightning")
    print("All Abilities: ")
    print(hero.abilities)