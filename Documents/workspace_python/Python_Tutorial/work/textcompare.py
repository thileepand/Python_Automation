import difflib
f = open('/home/thileepan/Downloads/projectfile/UAE0d37289.gif', 'r')
f1 = open('/home/thileepan/Downloads/projectfile/UAE0d37289.html', 'r')
str1 = f.read()
str2 = f1.read()
str1 = str1.split()
str2 = str2.split()
d = difflib.Differ()
diff = list(d.compare(str2,str1))
print ('\n'.join(diff))

def square(x):
        return x * x
print()
square(5)
