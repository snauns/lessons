from buildingerror import BuildingError
class Validation:
    def __init__(self, amount, limit):
        self.Amount = amount
        self.Limit = limit

    def Check(self):
        if (self.Amount > self.Limit):
            raise BuildingError(self.Amount, self.Limit)
            return True