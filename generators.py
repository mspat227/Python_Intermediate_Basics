#generators are functions that return a object that can  iterate over
#yeild is same like return but it will return one item at a time
#so it very memeory efivcient when its come to the large data sets
def my_generator():
    yield 1
    yield 2
    yield 3

g = my_generator()

#for i in g:
    #print(i)

#print(sum(g))

#if you need to print one by one yeild items then use next
#after the first yeild it will pause there and the the next one will be executed when the next next statement comes


value = next(g)
print(f"first yeild - {value}")

value = next(g)
print(f"second yeild - {value}")

value = next(g)
print(f"third yeild - {value}")