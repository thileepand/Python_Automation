"""
Tuple
like list but the are immutable
It means you can not change them
"""

my_list = [1,2,3,4,5]
print(my_list)

my_list[0] = 0
print(my_list)

print('**********************************')
my_tuple = (1,2,3,4,5,3,5,2)
print(my_tuple)

#my_tuple[0] = 0
#print(my_tuple)

print(my_tuple[0])
print(my_tuple[0:])

print(my_tuple.index(2))
print(my_tuple.count(3))