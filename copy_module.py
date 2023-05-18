#shallow and deep copy
# shallow copy is only one level deep, only referances of nested chiled objects
# deep copy is a full independent copy

import copy

#shallow copy

original = [1,2,3,4,5,6,7,8,9]
cpy = copy.copy(original)

#changing the value of copy, it will change only copy
cpy[0] = -10

print(original)
print(cpy)

#deep copy
original = [[10,20,30,40,50,60,70,80,90],[1,2,3,4,5,6,7,8,9]]
cpy = copy.deepcopy(original)

#changing the value of copy, it will change only copy, deep copy will move two dimentional
cpy[0][1] = -10

print(original)
print(cpy)
