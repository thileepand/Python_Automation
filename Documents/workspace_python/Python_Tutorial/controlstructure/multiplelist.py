"""
Iterating multiple list with the same time
"""

l1 = [1,2,3,4,5,6,7]
l2 = [6,7,8,10,15,20,25]

for a,b in zip(l1, l2):
    if a > b:
        print(a, end=" ")
    else:
        print(b, end=' ')