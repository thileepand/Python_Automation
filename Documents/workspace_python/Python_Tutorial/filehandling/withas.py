"""
With / AS Keywords
"""
#
# print("Normal write start")
# my_write = open("textfile.txt", "w")
# my_write.write("Trying to write to the file")
# my_write.close()
#
# print("Normal read start")
# my_read = open("textfile.txt", "r")
# print(str(my_read.read()))

print("With As Write Start")
with open("withas.txt", "w") as with_as_write:
    with_as_write.write("This is as example of write / read")

print()
print("with as ready start")
with open("withas.txt", 'r') as with_as_read:
    print(str(with_as_read.read()))