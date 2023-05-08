#lambda argument: expression

add10 = lambda x: x + 10
print(add10(5))

def add10_func(x):
    return x + 10
#above def function and lambda function does the same
#below is a eg on multiple arguments in lambda

multi = lambda x,y: x * y
print(multi(10,10))

def multi(x,y):
    return x * y


points = [(5,2), (3,11), (5,56), (124,8), (9,-1)]

points_sorted = sorted(points, key=lambda x: x[1])

print(points)
print(points_sorted)