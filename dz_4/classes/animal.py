from dz_4.classes.passanger import Passanger
from dz_4.classes.role import Role



class Animal(Passanger):

    def __init__(self, name):
        super().__init__(name, Role(1))

    def __str__(self):
        return f"{self.name} is {self.role}"