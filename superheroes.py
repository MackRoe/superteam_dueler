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


class Weapon(Ability):
    def attack(self):
        """  This method returns a random value
        between one half to the full attack power of the weapon.
        """
        half_damage = max_damage//2
        attack_now = random.randint(half_damage, self.max_damage)
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
        # and set starting values
        self.damage = 0
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
        """ Calculate the total damage from all ability attacks."""
        for each in self.abilities:
            # range only works with numbers
            self.damage = self.damage + each.attack()
        return self.damage

    def add_armor(self, armor):
        """ adds armor items to armors list """
        self.armors.append(armor)

    def defend(self, damage):
        """ Calculates total defense from armor """
        if len(self.armors) > 0:
           
            for each in self.armors:
                damage = damage - each.block(self)
            return damage
        else:
            return 0
    
    def take_damage(self, damage):
        """ Updates self.current_health to reflect the
        damage minus the defense. """
        defense = self.defend(damage)
        damage -= defense
        self.current_health = self.starting_health - damage

    def is_alive(self):
        """ Return True or False depending on whether the
        hero has been knocked out or not """
        
        if self.current_health <= 0:
            return False
        else:
            return True

    def fight(self, opponent):
        """ current hero fights each opponent until a champion is determined """
        
        while self.is_alive() and opponent.is_alive():
            if self.abilities == opponent.abilities:
                # declare a draw if combatant abilities are equivalent
                print("Hero abilities are equivalent. No victor possible.")
                print("Match declared a Draw")
            
            # attack opponent
            damage = self.attack()
            # accumulate opponent's damage
            opponent.take_damage(damage)
            # be attacked by opponent
            damage = opponent.attack()
            # be attacked by opponent
            self.take_damage(damage)
            
        if self.current_health > 0:
            print(self.name + " is victorious!")
        else:
            print(opponent.name + " is victorious!")
            

        
        
        # accumulate self damage
        
        # pass


class Team:
    def __init__(self, name):
        """ Initialize your team with its team name """
        self.name = name
        self.heros = []

    def add_hero(self, hero):
        self.heros.append(hero)
    
    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        #check that list is not empty
        if not len(self.heros) == 0
            index = self.heros.index(self.name)
            self.heros.pop(index)
        # finds index of hero name in list of heros
        # reference programiz.com


    def view_all_heros(self):
        for hero in self.heros:
            print(self.name)
        pass




if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    """ test code from tutorial """
    # 
    # print("Ability Name: " + ability.name)
    # print("Ability Strength: " + str(ability.attack()))
    # ability = Ability("Smite", 25)
    hero1 = Hero("Auntie M", 200)
    hero2 = Hero("The Coder")
    ability1 = Ability("Molecular Phasing", 100)
    ability2 = Ability("Hair Flip", 5)
    ability3 = Ability("Debugging Ability", 20)
    ability4 = Ability("Infinite Loop", 10)
    # whip = Armor("Whip", 30)
    # hero.add_armor(whip)
    # hero.take_damage(150)
    # print("Hero Name: " + hero.name)
    # print("Current Health: ", str(hero.current_health))
    # print("Alive?: ", hero.is_alive())
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    # print("All Abilities: ")
    # print(hero.abilities)
    # hero.take_damage(15000)
    # print("Damage: ")
    # print(hero.take_damage(1500)) #
    # print("Current Health: ") #
    # print(hero.current_health) #
    # print(hero.is_alive())
    hero1.fight(hero2)

