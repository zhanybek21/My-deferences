from functools import reduce
a = [1, 2, 3]
print(list(map(lambda x: x*2, a)))
print(list(filter(lambda x: x>1, a)))
print(reduce(lambda x, y: x+y, a))