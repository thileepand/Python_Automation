# def exp(x,n):
#     """
#
#     :param x:
#     :param n:
#     :return:
#     """
#     if n == 0:
#
#         return 1
#     else:
#         print(n)
#         return x * exp(x, n-1)
#
# exp(2,3)
from math import sin, cos, sqrt, atan2

R = 6373.0

lat1 = 52.2296756
lon1 = 21.0122287
lat2 = 52.406374
lon2 = 16.9251681

dlon = lon2 - lon1
dlat = lat2 - lat1
a = (sin(dlat/2))**2 + cos(lat1) * cos(lat2) * (sin(dlon/2))**2
c = 2 * atan2(sqrt(a), sqrt(1-a))
distance = R * c

print ("Result", distance)
print ("Should be", 278.546)


from math import radians, cos, sin, asin, sqrt
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [80.2462044, 12.9684718, 80.2464096, 12.9895733])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    km = 6367 * c
    return km
#print("Result", km)

haversine( 80.2462044, 12.9684718, 80.2464096, 12.9895733)