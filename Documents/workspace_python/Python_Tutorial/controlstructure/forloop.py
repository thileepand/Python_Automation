"""
Execute statement repeatedly
Condition are used to stop the execution of loop
Iterable items are Strings, List, Tuple, Dictionary
"""
#String for loop
my_string = 'abcabc'

for a in my_string:
    if a == 'a':
        print('A', end=' ')
    else:
        print(a, end=' ')

print()

#List for loop
cars = ['bmw', 'benz', 'honda']

for car in cars:
    print(car, end=' ')
print()

#List for loop
num = [1,2,3]

for n in num:
    print(n * 20)

print('*'*20)

#Dictionary for loop
d = {'one':1, 'two':2, 'three':3}
for k in d:
    print(k+ " "+str(d[k]), end=' ')
print()

print("*"*20)

for k,v in d.items():
    print(k, end=" ")
    print(v)