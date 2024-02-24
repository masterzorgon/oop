import random

class Insect:
    def __init__(self, type):
        self.wings = 2
        self.legs = 3
        self.flight_length = None 
        self.type = type

    def calc_length_of_flight(self):
        miles = random.randint(1, 10)
        self.flight_length = miles
    