# Encapsultion makes our public attribute to private means no one can change one object is intialized
#  by using double underscoe before variable name

class Enemy:

    def __init__(self,type_of_enemy,health_point=10,attact_damage=1):
        self.__type_of_enemy= type_of_enemy
        self.health_point=health_point
        self.attact_damage=attact_damage
        print('Enemy is created')


    def get_type_of_enemy(self):       # these get and set are called getter and setter in python
        return self.__type_of_enemy
    

    # def set_type_of_enemy(self,type_of_enemy):    # here it is not working as we have prohibted by using double underscore
    #     return self.__type_of_enemy = type_of_enemy


    def talk(self):
        print("I am an Enemy")
