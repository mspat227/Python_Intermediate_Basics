def print_name(name):
    print(name)
#above name is the parameter in the function
#below "alex" is the argument

print_name("Alex")

#positional arguments and key word arguments

def foo(a, b, c):
    print(a,b,c)
#positional arguments
foo(1,2,3)

#keyword arguments (order matters)/ also called named arguments
foo(a=1, b=2, c=3)
foo(c=1, b=2, a=3)

#if mix the positional arguments with keyword args then only positional args follows by keyword args
foo(1 , c=2, b=3)

#default arguments
#default argumrnts only can be add after the non-default arguments

def bar(a, b, c, d=4):
    print(a, b, c, d)

bar(1, 2, 3)
#but if you add one more arguments to bar func then it will print insted default value
bar(1,2,3,5)

#variable length arguments

#if you add *args in to parameter you can add any numbers of positional arguments to function without mentioning
#if you add **kwargs in to parameter you can add any numbers of key word arguments to function without mentioning
#args are tuple
#kwargs are dicts

def baz(a, b, *args, **kwargs):
    print(a, b)
    for i in args:
        print(i)
    for key in kwargs:
        print(key, kwargs[key])

baz(1,2,3,4,5,6, seven=7, eight=8, nine=9, ten=10)