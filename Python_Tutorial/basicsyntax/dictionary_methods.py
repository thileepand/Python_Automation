"""
Dictionary methods
"""

car = {'make':'bmw', 'model':'550i', 'year':'2016'}
cars = {'bmw':{'model':'550i', 'year':'2016'}, 'benz':{'model':'E330', 'year':'2015'}}
print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())
print(cars.items())

car_copy = car.copy()
print(car_copy)
#car.clear()

print(car.pop('model'))
print(car)