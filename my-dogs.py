import dog

my_dog = dog.Dog("Rex", "superdog")
my_dog.bark()

my_other_dog = dog.Dog("Annie", "superdog")
print("My other dog's name is: " + my_other_dog.name)

third_dog = dog.Dog("Kitty", "poodle")

my_other_dog.sit()
third_dog.roll_over()