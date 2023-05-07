# Collections: Counter, namedtuple, OrderedDict, defaultdict, deque

from collections import *

'''
collections documentation

https://docs.python.org/3/library/collections.html?highlight=collections#collections.deque
'''

#Counter
a = "aaaaaaaabbbbbbsssssbbbffffkkkeeeeee"

my_counter = Counter(a)
#print how many times the element repeats
print(my_counter)
#print most_common first two elements
print(my_counter.most_common(2))
#get the most common first element and first value of the tuple(0 index / starting from 0)
print(my_counter.most_common(2)[0][0])
#making string into a list
print(list(my_counter.elements()))

#namedtuple
#this will create a simple class

Point = namedtuple("Point", "x,y,z")
pt = Point(1, 2, 3)
print(pt)
print(pt.x, pt.y, pt.z)

#OrderedDict
#this will remember the order we add the elements
ordered_dict = OrderedDict()
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
ordered_dict["e"] = 5
ordered_dict["f"] = 6

print(ordered_dict)

#defaultDict
#if the key is not set this dict will have a default value

