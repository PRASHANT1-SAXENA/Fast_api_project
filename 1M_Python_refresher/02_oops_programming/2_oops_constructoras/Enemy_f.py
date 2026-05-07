class Enemy:

    def __init__(self,type_of_enemy,health_point=10,attact_damage=1):
        self.type_of_enemy= type_of_enemy
        self.health_point=health_point
        self.attact_damage=attact_damage
        print('Enemy is created')

    def talk(self):
        print("I am an Enemy")


    