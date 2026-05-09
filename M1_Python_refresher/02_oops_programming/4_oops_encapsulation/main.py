# Encapsultion makes our public attribute to private means no one can change one object is intialized
#  by using double underscore before variable name and you can see that with getter as well not directly

from Enemy_f import *

zombiee= Enemy('Zombiee',12,6)

print(zombiee.__type_of_enemy) # does work here as can not access with a getter and not able to change directly neither setter
print(zombiee.get_type_of_enemy())
print(zombiee.health_point)
print(zombiee.attact_damage)


