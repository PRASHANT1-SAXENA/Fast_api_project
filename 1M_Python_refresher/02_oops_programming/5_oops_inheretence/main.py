from Enemy_f import *


# Objects
animal = Animal()
dog = Dog()
bird = Bird()


animal.sound()   # Animal makes a sound


dog.sound()   # Overridden
dog.eat()     # Parent method
dog.run()     # Dog method

bird.sound()  # Overridden
bird.eat()    # Parent method
bird.fly()    # Bird method


s1 = Student("Prashant", 25, "B.Tech")

print(s1.name)
print(s1.age)
print(s1.degree)