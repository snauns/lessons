from Human import Human
from auto import Auto
kyrylo = Human("Kyrylo", 1)
nikita = Human("Nikita", 0)
mykhailo = Human("Mykhailo", 0)
pavlo = Human("Pavlo", 0)
humans = list()
humans.append(kyrylo)
humans.append(mykhailo)
humans.append(pavlo)
humans.append(nikita)
auto = Auto("BMW X7")
for human in humans:
    if(human.Role == 1):
        auto.AddDrivers(human.Name)
    else:
        auto.AddPassengers(human.Name)
for driver in auto.Drivers:
    auto.ToStringDriver(driver)
for passenger in auto.Passengers:
    auto.ToStringPassenger(passenger)