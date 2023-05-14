import random

#creating a random float between 0-1
a = random.random()
print(a)

#creating a random float in a specific range
b = random.uniform(1, 10)
print(b)

#crearing a random int including the upperbound(10)
c = random.randint(1,10)
print(c)

#creating a random int excluding upper bound
d = random.randrange(1, 10)
print(d)

#choosing random item from list
my_list = list("ABCDEFGHIJ")
e = random.choice(my_list)
print(e)

#choosing multiple items(sample size is 4)
f = random.sample(my_list, 4)
print(f)

#choosing items with duplicates(sample size 3)
g = random.choices(my_list, k=3)
print(g)

#shuffeling items
random.shuffle(my_list)
print(my_list)

'''
random seed
'''
random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(1)
print(random.random())
print(random.randint(1,10))

random.seed(2)
print(random.random())
print(random.randint(1,100))

random.seed(2)
print(random.random())
print(random.randint(1,100))

#random seed 1 will give same random numbes were
# ever you run code unless use two or more