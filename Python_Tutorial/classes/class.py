"""
Object Oriented Programming
"""

class Car(object):

    def __init__(self, make, model='550i'):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car:" + self.make)
        print("Model of the car:" + self.model)

c1 = Car('bmw')
# print(c1.make)
# print(c1.model)
c1.info()

c2 = Car('benz')
c2.info()
# print(c2.make)
# print(c2.model)

