"""
Position parameter
They are like optional parameter
And can be assigned to default value, if no value provided from outside
"""

def sum_num(n1=15, n2=16):
    """
    :param n1:
    :param n2:
    :return:
    """
    return n1 + n2
sum1 = sum_num(n2=20, n1=30)
print(sum1)