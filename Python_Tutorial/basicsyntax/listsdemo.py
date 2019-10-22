"""
Data type to store more than one value in one variable name
List item are in brackets, separated with ","[1,2,3]
"""
cars = ["bmw","honda","audi"]
print(cars)
print("*"*20)
print(cars[2])


num_list = [1,2,3,4,5]
sum_num = num_list[0] + num_list[4]
print(sum_num)

more_cars = ["bmw","honda","audi"]
print(more_cars[1])

more_cars[0]="benz"
print(more_cars[0])
print(more_cars)