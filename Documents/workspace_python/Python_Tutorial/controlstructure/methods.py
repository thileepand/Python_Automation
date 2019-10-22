"""
A group of code statement which can perform some specific task
 Methods are reusable and can be called when needed in the code
"""

def sum_num(n1, n2):
    """
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2

sum1 = sum_num(15, 17)
sum2 = sum_num(35, 45)

string_add=sum_num('one','two')
print(string_add)

print(sum1)
print(sum2)

print('***************************')

def isMetro(city):
    l = ['chennai','mumbai','bangalre']

    if city in l:
        return True
    else:
        return False

x = isMetro('kovai')
print(x)

print('***************************')

def isCars(available):
    l = ['bmw','honda','benz','jeep']

    if available in l:
        print('available')
    else:
        print('not available')

x = isCars('jeep')
print(x)
