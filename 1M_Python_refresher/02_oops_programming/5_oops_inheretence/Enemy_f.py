class Animal:
    def sound(self):
        print("Animal makes a sound")

    def eat(self):
        print("Animal eats food")


class Dog(Animal):
    def sound(self):   # Overriding
        print("Dog barks")

    def run(self):
        print("Dog runs fast")


class Bird(Animal):
    def sound(self):   # Overriding
        print("Bird chirps")

    def fly(self):
        print("Bird flies in sky")


dog = Dog()
bird = Bird()

dog.sound()   # Overridden
dog.eat()     # Parent method
dog.run()     # Dog method

bird.sound()  # Overridden
bird.eat()    # Parent method
bird.fly()    # Bird method





# with overriding 


# with super 

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, degree):
        super().__init__(name, age)   # Parent constructor who is use to define name and age it used from parent class by using super
        self.degree = degree


