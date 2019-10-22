class Car(object):

    def __init__(self):
        print("You just created the car instance")

    def start(self):
        print("You started the car")

    def speed(self):
        print("You are driving over speed")

    def stop(self):
        print("Stopped the car")


class bmw(Car):
    def __init__(self):
        Car.__init__(self)

    def speed(self):
        super(bmw, self).speed()
        print("driver don't have the experience")

    def slow(self):
        print("slow the car")


c = Car()
c.start()
c.speed()
c.stop()

b = bmw()
b.speed()
b.slow()

