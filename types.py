from timeit import default_timer as timer

#Dictionaries

print("Dictionaries => Key-Value pairs, Unordered, Mutable ")
my_dict = {'mayura':9, 'age':16, 'dummy':81}
print(my_dict['mayura'])
print(my_dict.keys())
print(my_dict.values())

#Sets
print("Sets => Unorderd, Mutable, No Duplicates")

my_set = {1, 2, 3, 4, 4}
my_set.add(5)
#dublicate 4 is ignored
print(my_set)

'''
Set Methods
Method	                Description
add()	                Adds an element to the set
clear()	                Removes all the elements from the set
copy()	                Returns a copy of the set
difference()	        Returns a set containing the difference between two or more sets
difference_update()	    Removes the items in this set that are also included in another, specified set
discard()	            Remove the specified item
intersection()	        Returns a set, that is the intersection of two or more sets
intersection_update()	Removes the items in this set that are not present in other, specified set(s)
isdisjoint()	        Returns whether two sets have a intersection or not
issubset()	            Returns whether another set contains this set or not
issuperset()	        Returns whether this set contains another set or not
pop()	                Removes an element from the set
remove()	            Removes the specified element
symmetric_difference()	Returns a set with the symmetric differences of two sets
symmetric_difference_update()	inserts the symmetric differences from this set and another
union()	                Return a set containing the union of sets
update()	            Update the set with another set, or any other iterable

'''

#Strings
print("Strings => Ordered, Immutable, Test representation")
my_string = "Hello World"

#select 1 - 5 elements in string excluding 5th element
new = my_string[1:5]
print(new)

#select every second element but by default its 1
new1 = my_string[::2]
print(new1)

#select every element from the end
new2 = my_string[::-1]
print(new2)

new3 = my_string[::-2]
print(new3)

print(my_string.count("l"))

#string join method

my_list = ["m"] * 10
#print(my_list)

#bad python method
start = timer()
new_string= ""
for i in my_list:
    new_string += i
stop = timer()
print(stop-start)

#good python method
start = timer()
new1_string = "".join(my_list)
stop = timer()
print(stop-start)
#closley monitor the timing of the two diffetent methods(when list is 1000000 times)
# bad method took 47.91 seconds
# good method took 0.00781 seconds

#format string
var = 3.23564365837453853

#adding only the first two decimal points
my_new_string = f"Hello World {var:.2f}"
print(my_new_string)