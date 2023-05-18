#********
#usage of astriks *

#Multification
result = 7 * 7
print(result)

#power of
result = 2 ** 4
print(result)

#repeated operations in lists
zeros = [0] * 10
print(zeros)

zeros = [0, 1, 2] * 10
print(zeros)

#repeated operation in tuples
zeros = (0) * 10
print(zeros)

zeros = (0, 4 , 5) * 10
print(zeros)

#string
string = "AB" * 10
print(string)

#args and kwargs
def foo(a,b,*args, **kwargs):
    print(a,b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])
foo(1,2,3,4,5, hello= 10, world= 15)

#unpacking list
numbers = [1,2,3,4,5,6,7]

*beginning,  last = numbers

print(beginning)
print(last)

#unpacking tuple( but will return a list)
numbers = (1,2,3,4,5,6,7)

beginning, *middle, secondlast, last = numbers

print(beginning)
print(middle)
print(secondlast)
print(last)

#merge tuple, sets, lists
my_tuple = (1,2,3,4,5,6,7)
my_list = [8,9,10,11,12,13,14]
my_set = {15,16,17,18,19,20,21}
new_list = [*my_tuple, *my_list, *my_set]
print(new_list)

#merge dicts

dict_a = {"a": 1, "b":2}
dict_b = {"c":3, "d":4}

new_dict = {**dict_a, **dict_b}
print(new_dict)