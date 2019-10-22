    def foo():
        #do something

    def decorator(func):
        # manipulate func
        return func

    foo = decorator(foo) #manualy decorate

    @decorator
    def bar():
        #do something

     # bar() is decorators

