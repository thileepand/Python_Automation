"""
File I/O
 'W' -> Write Only Mode
 'R' -> Read only Mode
 'R+' -> Ready and Write
 'A' -> Append Mode
"""

my_list = ["first line","second line","third line"]
my_file = open("firstfile.txt", "w")

for item in my_list:
    my_file.write(str(item) + "\n")

my_file.close()

