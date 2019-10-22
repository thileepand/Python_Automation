"""
Examples to show available methods in python

"""
#Accessing characters in a string
#Index start from zero
first = "nyc"[0]
city = "sfo"
print(first)
fr = city[0]
print(fr)

"""
len()
lower()
upper()
str()
"""
stri = "This Is a Mixed Case"
print(stri.lower())
print(stri.upper())
print(len(stri))

print(stri + str(2))

"""
Concatenation
"""
print("Hello "+" world!!")
print(first + " " + city)