"""
Built-in methods to help manipulating a list
"""

cars = ["bmw","honda","audi"]
length = len(cars)
print(length)

cars.append("benz")
print(cars)

cars.insert(0,"sumo")
print(cars)

x = cars.index("audi")
print(x)

y = cars.pop()
print(y)
print(cars)

cars.remove("sumo")
print(cars)

slicing = cars[0:2]
a = cars[1:len(cars)]
print(slicing)
print(a)
print(cars)
cars.sort()
print(cars)