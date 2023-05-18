from dz_3.classes.animal import Animal
from dz_3.classes.auto import Auto
from dz_3.classes.human import Human
from dz_3.classes.role import Role

my_auto = Auto("Mercedes", Human("Kirill", Role(0)))
my_auto.addPassenger(Human("Andrey", Role(1)))
my_auto.addPassenger(Human("Nikita", Role(1)))
my_auto.addPassenger(Human("Misha", Role(1)))
my_auto.addPassenger(Animal("Dog"))

print(my_auto)
