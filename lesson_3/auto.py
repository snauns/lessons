class Auto:
    def __init__(self, brand = None):
        self.Brand = brand
        self.Passengers = list()
        self.Drivers = list()
    def AddPassengers(self, human):
        self.Passengers.append(human)
    def AddDrivers(self, human):
        self.Drivers.append(human)
    def ToStringDriver(self, driverName):
        print(f"Driver of: {self.Brand} is {driverName}")
    def ToStringPassenger(self, passengerName):
        print(f"Passenger of: {self.Brand} is {passengerName}")