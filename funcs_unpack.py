#unpacking the lists/tuple into function arguments
#length of the lists/tuple must be same number of elements

def foo(a,b,c):
    print(a,b,c)

my_list = [1,2,3]

foo(*my_list)

#unpacking the dict into function arguments

def bar(a,b,c):
    print(a,b,c)

#dict key should be the same function parameters
#length of the dict must be same number of elements
my_dict = {"a": 1, "b": 2, "c": 3}

bar(**my_dict)