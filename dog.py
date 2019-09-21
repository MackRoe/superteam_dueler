# dog.py
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        print("woof!")
    def sit(self):
        print(self.name + " sits")
    def roll_over(self):
        print(self.name + " rolls over")

