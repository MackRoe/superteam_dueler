class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print("{} is eating".format(self.name))
    
    def drink(self):
        print(self.name + " is drinking.")
    
animal = Animal("cat")
animal.eat()
animal.drink()