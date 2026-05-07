from Enemy_f import *

# making a funciton to take one 
def animal_actions(animal):
    animal.sound()
    animal.move()


a = Animal()
d = Dog()
b = Bird()

animal_actions(a)
animal_actions(d)
animal_actions(b)