from dz_4.classes.creature import Creature


class Passanger(Creature):

    def __init__(self, name, role):
        super().__init__(name)
        self.role = role

    def __str__(self):
        return f"{super().__str__()} is {self.role}"