"""
Object Oriented Programming
"""

class Car(object):

    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car stared...")

    def stop(self):
        print("Car stopped")


class bmw(Car):

    def __init__(self):
        Car.__init__(self)
        print("You just created the bmw instance")


c = Car()
c.drive()
c.stop()

b = bmw()
c.drive()
c.stop()
