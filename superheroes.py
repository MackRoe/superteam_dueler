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
        half_damage = self.max_damage//2
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
        self.deaths = 0
        self.kills = 0
        self.abilities = []
        self.armors = []
        # abilities and armors are lists that
        # will contain objects
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

    def add_weapon(self, weapon):
        """ adds weapon abilities to abilities list """
        self.abilities.append(weapon)

    def defend(self):
        """ Calculates total defense from armor """
        defense = 0
        if len(self.armors) > 0:
            for each_armor in self.armors:
                defense += each_armor.block()
            return defense
        else:
            return 0
    
    def take_damage(self, damage):
        """ Updates self.current_health to reflect the
        damage minus the defense. """
        defense = self.defend()
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
            self.add_kill()
            opponent.add_death()
        else:
            print(opponent.name + " is victorious!")
            self.add_death()
            opponent.add_kill()

    def add_kill(self):
        """ update number of kills """
        # tutorial says to also use a num_kills (?) parameter
        self.kills += 1

    def add_death(self):
        """ update number of deaths """
        # tutorial says to also use a num_deaths (?) parameter
        self.deaths += 1


class Team:
    def __init__(self, name):
        """ Initialize your team with its team name """
        self.name = name
        self.heroes = []

    def add_hero(self, hero):
        self.heroes.append(hero)
    
    def remove_hero(self, name):
        '''Remove hero from heroes list.
        If Hero isn't found return 0.
        '''
        #check that list is not empty
        if not len(self.heroes) == 0:
            index = self.heroes.index(self.name)
            self.heroes.pop(index)
        # finds index of hero name in list of heroes
        # reference programiz.com

    def view_all_heroes(self):
        for hero in self.heroes:
            print(self.name)

    def get_living_heroes(self):
        living_heroes = []
        for hero in self.heroes:
            if Hero.is_alive(hero):
                living_heroes.append(hero)
                return living_heroes

    def make_other_team(self, heroes):
        """ sorts every other hero into other team """
        self.other_team = []
        # sort into teams
        for hero in heroes:
            index = heroes.index(hero)
            if heroes(index) % 2:
                self.other_team.append(hero)
                self.heroes.pop(hero)
        return self.other_team

    def random_hero(self, heroes):
        """ gets random hero from list of heroes """
        return random.choice(heroes)

    def attack(self, other_team): 
        """ battle teams against each other """
        # select random hero
        hero_team1 = Team.random_hero(self.heroes)
        hero_team2 = Team.random_hero(self.other_team.heroes)
        # check that selected hero is alive
        while hero_team1.is_alive() and hero_team2.is_alive():
            hero_team1.fight(hero_team2)

    def revive_heroes(self, health=100):
        """ reset the health of all heroes back to starting health """
        for hero in self.heroes:
            self.health = health
            hero.current_health = hero.starting_health

    def stats(self):
        """ print team stats """
        for hero in self.heroes:
            print("{}: Kills: {}, Deaths {}".format(self.name, self.kills, self.deaths))


class Arena:
    def __init__(Hero):
        self.arena_team1 = []
        self.arena_team2 = []
        self.weapons = []

    def create_ability(self):
        """ prompt user for ability info
        & return ability values """
        added_ability = input("What is the name of your hero's ability? ")
        print("What is the maximum amount of damage this ability")
        added_ability_max_damage = input("is capable of inflicting? ")
        return Ability(added_ability, added_ability_max_damage)

    def create_weapon(self):
        '''Prompt user for Weapon information
            return Weapon with values from user input.
        '''
        added_weapon = input("What is your hero\'s weapon? ")
        print("What is the maximum damage that your hero\'s weapon")
        added_weapon_max_damage = input("is capable of inflicting? ")
        return ability(added_weapon, added_weapon_max_damage)

    def create_armor(self):
        added_armor = input("What armor does your hero use? ")
        added_armor_max_defense = input("How much damage can it deflect? ")
        return armor(added_armor, added_armor_max_defense)

    def create_hero(self, name, abilities, armors, weapons):
        '''Prompt user for Hero information
          return Hero with values from user input.
        '''
        
        # get hero's name
        if len(heroes) < 2:
            name = input("What is your hero's name? ")
            add_hero(name)
            while not name == "":
                run_create_ability = input("Does your hero have a special ability? [Y or N] ")
                
                while not run_create_ability == "":
                    if upper.run_create_ability == "Y":
                        create_ability()
                    elif not upper.run_create_ability == "N":
                        print("Ok")
                    else:
                        name = ""

                run_create_armor = input("Does your hero have armor? [Y or N]")
                while not run_create_armor == "":
                    if upper.run_create_armor == "Y":
                        create_armor()
                    elif not upper.run_create_armor == "N":
                        print("Ok")
                    else:
                        name = ""

                run_create_weapon = input("Does your hero have armor? [Y or N]")
                while not run_create_weapon == "":
                    if upper.run_create_weapon == "Y":
                        create_weapon()
                    elif not upper.run_create_weapon == "N":
                        print("Ok")
                    else:
                        name = ""
        else:
            print("Minimum Two Heroes Required :: Fatal Error - Program Quit")
        # create a hero object that contains abilities, armors, and weapons
        return hero(name, ability, armor, weapon)

        # examine list item names for correct correlation 
    
def build_team_one():
    '''Prompt the user to build team_one '''
    print("Build Team One")
    team_size = input("How many heroes will be in Team One? ")
    while not done == True:
        self.create_hero()
        self.arena_team1.append(self.hero)
        ask1 = input("Create another hero?" [Y or N])
        if upper.ask == "N":
            done == True

def build_team_two():
    ask2 = input("Build Team Two [type an \'x\']")
    if not ask2 == "x":
        ask2 = input("Build Team Two [type an \'x\']")
    else:
        team_size = input("How many heroes will be on Team Two? ")
        count = 0
        if count < (team_size - 1):
            self.create_hero()
            self.arena_team2.append(self.hero)
        else:
            print("Teams are Built")


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

