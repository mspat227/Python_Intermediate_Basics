# map(function, seq)

a = [1,2,3,4]

b = map(lambda x: x*2, a)

print(list(b))

# list comprehention

c = [x * 2 for x in a]

print(c)