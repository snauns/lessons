from dz_3.classes.role import Role


class Animal:

    def __init__(self, name):
        self.name = name
        self.role = Role(1)

    def __str__(self):
        return f"{self.name} is {self.role}"