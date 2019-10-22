"""
Variable scope
"""
a = 10

def test_method(a):
    print("value of local a is:" + str(a))
    a = 5
    print("New value of local a is:" + str(a))

print("value of global a is:" + str(a))

test_method(a)
print("Did you changed global a change?" + str(a))


a = 10

def test_method():
    global a
    print("value of 'a' inside the method is:" + str(a))
    a = 5
    print("New value of 'a' inside the method changed to:" + str(a))

print("value of global a is:" + str(a))
test_method()
print("Did you changed global a change?" + str(a))