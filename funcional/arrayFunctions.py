# map
import functools

lista = [1, 2, 3]
m = map(lambda x: x**2, lista)

for i in m:
    print(i)


lista2 = [1, 2, 2 , 63, 12, 42]

reducer = functools.reduce(lambda x, y: x + y, lista2)

print(reducer)

filter_ = filter(lambda x: x%2 == 0, range(10))

for i in filter_:
    print(i)