from Enemy_f import *

enemy1=Enemy()
enemy2=Enemy()

enemy2.health_points=100

print(enemy1.health_points) # output 10
print(enemy2.health_points) # output 100


# print(enemy1.type_of_enemy)  # it give error as it undefined means no value only intialize in class

enemy1.type_of_enemy="zombie"

print(enemy1.type_of_enemy)