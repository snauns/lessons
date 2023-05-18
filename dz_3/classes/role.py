class Role:

    def __init__(self, role_type):
        self.role_type = role_type

    def __str__(self):
        if self.role_type == 0:
            return "Driver"
        elif self.role_type == 1:
            return "Passenger"
        else:
            return "Unknow"

    def isDriver(self):
        return self.role_type == 0