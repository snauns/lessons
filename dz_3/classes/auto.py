
class Auto:
    def __init__(self, brand, driver):
        self.brand = brand
        if driver.role.isDriver():
            self.driver = driver
        else:
            raise Exception(f"{driver} cannot be a driver")
        self.passengers = list()

    def addPassenger(self, passenger):
        if passenger.role.isDriver():
            raise Exception(f"only one driver can be in the car, {passenger}")
        else:
            self.passengers.append(passenger)

    def __str__(self):
        result_str = f"{self.brand}\n{self.driver}\n"
        for psngr in self.passengers:
            result_str = f"{result_str}{psngr}\n"
        return result_str


