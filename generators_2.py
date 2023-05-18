import sys
import timeit

#old school :)
def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

#generator
def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sum(firstn(10)))
print(sum(firstn_generator(10)))

print("memory usage")
#now lets see how much memory ech use to ge the same result in larg scale data set

print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))