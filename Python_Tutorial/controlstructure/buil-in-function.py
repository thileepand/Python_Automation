"""
Some built-in-function
max(): It takes any number of arguments and returns the largest one.

min(): It takes any number of arguments and returns the smallest one.

abs(): It returns absolute value of the number, that number distance from 0.
It always returns a positive value and its only takes a single number

type(): It returns the type of the data it receive as an arguments
"""
#max(): It takes any number of arguments and returns the largest one.
def largest_num(*args):
    print(max(args))
    return (max(args))

largest_num(-20, -10, 0, 10, 109)

#min(): It takes any number of arguments and returns the smallest one.
def smallest_num(*args):
    print(min(args))

smallest_num(-20, -10, 0, 10, 109)

#abs(): It returns absolute value of the number, that number distance from 0
def abs_function(a):
    print(abs(a))

abs_function(-50)
abs_function(20)

print('**********************')
#type(): It returns the type of the data it receive as an arguments
print(type(99))
print(type(99.99))
print(type('99.9'))
l = [1, 2, 3]
print(type(l))