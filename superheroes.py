import random

""" code under construction """

class Ability:
    def __init__(self, name, attack_strength):
        # instance variables
        self.name: name
        self.max_damage: max_damage
    def attack(self):
        print(self.name + " attacks!")
        attack_now = random.randint(0, max_damage)
        return attack_now


new_hero = Ability("Smite", 25)

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    """ test code from tutorial """
    ability = Ability("Debugging Ability", 20)
    print(ability.name)
    print(ability.attack())