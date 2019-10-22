"""
Built-in function
Creates a sequence of numbers but does not save them in memory
Very use for generating the numbers
"""

a = range(0, 20, 2)
print(a)
print(type(a))
print(list(a))

l = [1,2,3]
for num in range(1, 5):
    print(num)

print("#"*30)
# Demo of using strip method

str_a = "      Python is Outstanding      "

str_b = str_a.strip()

print("The Original String:", str_a)

print("With strip method:", str_b)

str_b = str_a