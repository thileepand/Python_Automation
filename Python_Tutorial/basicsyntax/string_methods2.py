"""
Examples to show available string methods in python
"""
#Replace methods
a = "1abc2abc3abc"
print(a.replace('abc', 'ABC',1))

#Sub-string
#Starting index is exclusive
#Ending index is exclusive
sub = a[1:10]
print("******************")
print(sub)
step = a[1:10:3]
print(step)