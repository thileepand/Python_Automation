"""
https://docs.python.org/3/library/
"""
import math
from math import sqrt
#import modulesexternal.car as car
from modulesexternal.car import info

class Modules():

    def builtin_modules(self):
        print(math.sqrt(150))
        print(sqrt(100))

    def car_description(self):
        make = "bmw"
        model = "550i"
        info(make,model)


m =Modules()
m.builtin_modules()
m.car_description()