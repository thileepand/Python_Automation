"""
Exception are error
We should handle exception in our code
to make sure the code is working the way we want and is handling all the unwanted issues.
Link to 3.4 built-in exception - https://docs.python.org/3/library/exception.html
"""

def exceptionHandling():
    try:
        a = 10
        b = 'safd'
        c = 10

        d = (a + b) / c
        print(d)
    except ZeroDivisionError:
        print("Zero Division")

    except TypeError:
        print("string not possible to convert to int")

exceptionHandling()




def exceptionHandling():
    try:
        a = 10
        b = 20
        c = 0

        d = (a + b) / c
        print(d)
    except:
        print("In the except block")
    else:
        print("Because there was no exception, else is executed")
    finally:
        print("Finally, always executed")

exceptionHandling()