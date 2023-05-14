from human import Human
from speak import Speak

class ItStepStudent(Human):

    def __init__(self, group, avgGrade, name, age, height):
        super().__init__(name, age, height)
        self.Group = group
        self.AvgGrade = avgGrade
        self.SayName = name

    def __str__(self):
        return f"{super().__str__()}Group: {self.Group}\nAvg grade: {self.AvgGrade}"