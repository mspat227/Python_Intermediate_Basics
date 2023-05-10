#Errors and exceptions
x = -5

#assert (x>=0), 'x is not positive'

#if no exceptions, else and finnally will be executed
#if exception True then exception and finally will be excecuted
try:
    a = 5/1
    b = a + '4'
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine")
finally:
    print("Cleaning up")