"""
Create fruit class and 3 method
Once create the parent class then call the child class
"""

class Fruit(object):

    def __init__(self):
        print("I am a fruit")

    def nutrition(self):
        print("I am full of vitamin")

    def fruit_shap(self):
        print("Every fruits can have  different shape")


class Mango(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("I am mango")

    def nutrition(self):
        print("I am a full of vitamin c")

    def color(self):
        print("The color is also yellow")


a = Fruit()
a.nutrition()
a.fruit_shap()


b = Mango()
b.nutrition()
b.color()