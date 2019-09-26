import random

""" code under construction 
    This program is assigned practice within
    school curriculum """


class Ability:
    def __init__(self, name, attack_strength):
        """ instance variables
            name: str
            max_damage: int """
        self.name = name
        self.max_damage = attack_strength

    def attack(self):
        # print(self.name + " attacks!")  -- outside of specs --
        attack_now = random.randint(0, self.max_damage)
        # creates a randomly rated attack
        return attack_now


class Armor:
    def __init__(self, name, max_block):
        """ Instance Variables
            name: str
            max_block: int
        """
        self.name = name
        self.max_block = max_block

    def block(self):
        block = random.randint(0, self.max_block)
        return block
        # creates a randomly rated blocking action    
        

class Hero:
    def __init__(self, name, starting_health=100):
        # Initialize instance variables values as instance variables
        self.damage = 0
        # abilities = []
        # armors = []
        # set starting values
        self.abilities = []
        self.armors = []
        # abilities and armors are lists that will contain objects
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
       

    def add_ability(self, ability):
        self.abilities.append(ability)
        """ Add ability to abilities list """
        # return abilities

    def attack(self):
        # , name, attack_strength
        for each in range(abilities):
            total_damage = damage + Ability.attack()
            return total_damage

    def add_armor(self, armor):
        """ adds armor items to armors list """
        self.armors.append(armor)

    def defend(self, damage):
        """ Calculates total defense from armor """
        if len(self.armors) > 0:
            block = 0
            for each in self.armors:
                block = block + each.block()
                return block
        else:
            return 0
    
    def take_damage(self, damage):
        """ Updates self.current_health to reflect the
        damage minus the defense. """
        defense = hero.defend(damage)
        damage -= defense
        self.current_health = self.starting_health - damage

    def is_alive(self):
        """ Return True or False depending on whether the 
        hero has been knocked out or not """
        
        if hero.current_health <= 0:
            return False
        else:
            return True

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    """ test code from tutorial """
    # ability = Ability("Debugging Ability", 20)
    # print("Ability Name: " + ability.name)
    # print("Ability Strength: " + str(ability.attack()))
    # ability = Ability("Smite", 25)
    hero = Hero("Auntie M", 200)
    # whip = Armor("Whip", 30)
    # hero.add_armor(whip)
    hero.take_damage(150)
    print("Hero Name: " + hero.name)
    print("Current Health: ", str(hero.current_health))
    print("Alive?: ", hero.is_alive())
    # hero.add_ability("Force Wave")
    # hero.add_ability("Lightning")
    # print("All Abilities: ")
    # print(hero.abilities)
    # hero.take_damage(15000)
    # debug to discover why damage is not being received
    # print("Damage: ")
    print(hero.take_damage(1500)) #
    print("Current Health: ") #
    print(hero.current_health) #
    print(hero.is_alive())

