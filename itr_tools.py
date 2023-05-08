# itertools: product, permutations, combinations, accumulate, groupby and infinite operators

from itertools import *

#product
a = [1,2]
b = [3,4]

#[product will give a nested for loop in a and b and we can give argument of how many tims to repeate. default is 1]
prod = product(a,b, repeat=2)

#to show the result we need to convrt to list
print(f"Product = {list(prod)}")

#permutation - this will give a possible orderings of a list or any

c = [1,2,3]

#second argument we can give is to what is the macimum length of iterable
perm = permutations(c,2)
#to see we have to convert to list or any
print(f"Permutations = {list(perm)}")

#combinations = all possible combinations

d = [1,2,3,4]

#here the second argument is mandatory(lenghth of combinartion)
comb = combinations(d, 2)

print(f"Combinations = {list(comb)}")

#accumulate - Make an iterator that returns accumulated sums, or accumulated results of other binary functions

e =[1,2,3,4]
#1, 1+2, 1+2+3, 1+2+3+4

acc = accumulate(e)

print(f"Accumulate = {list(acc)}")

#groupby - Make an iterator that returns consecutive keys and groups from the iterable.

def smaller_than_3(x):
    return x < 3

f =[1,2,3,4]

#lamda will do the same like above function
group_obj = groupby(f, key=lambda x: x < 3)
for key, value in group_obj:
    print(key, list(value))

'''
itertools documentation - https://docs.python.org/3/library/itertools.html?highlight=itertoo#itertools.groupby
'''