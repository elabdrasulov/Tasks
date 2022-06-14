# Task 1

a = {'x': 1, 'y': 2, 'z': 1}
list_ = list(a)
print(list_[0])


# Task 2

a = {'a': 1, 'b': 2, 'c': 1}
popped = a.pop('a')
print(popped)


# Task 3

a = {'a': 1, 'b': 2, 'c': 1}
a2 = {'f': 55}
a.update(a2)
print(a)


# Task 4

a = {'a': 1, 'b': 2, 'c': 1}
a.clear()
print(a)


# Task 5

a = {'a': 1, 'b': 2, 'c': 1}
l = list(a)
print(l)


# Task 6

a = {'a': 1, 'b': 2, 'c': 1}
b = a.copy()
print(b)


# Task 7

a = {'a': 1, 'b': 2, 'c': 1}
for k in a:
    print(k)


# Task 8

a = {'a': 1, 'b': 2, 'c': 1}
for k, v in a.items():
    print(v)


# Task 9

a = {'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6}
b = a.copy()

for k, v in list(b.items()):
    if v % 2 == 0:
        b[k] = 2

print(b)


# Task 10

a = {'a': None, 'b': 1, 'c': 2, 'd': None, 'e': 3}

for k, v in list(a.items()):
    if v == None:
        del a[k]
        
print(a)


# Task 11

a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 

for k, v in list(a.items()):
    a[k] = v / 5

print(a)

# Task 12

a = {'apple': 2, 'orange': 5, 'banana': 10} 

for k, v in list(a.items()):
    if v % 2 == 0:
        del a[k]

print(a)


# Task 13

a = {'a': 1, 'b': 2, 'c': 3}

swapped = dict((v, k) for k, v in a.items())
print(swapped)

# Task 13 (#2)

# a_swapped = dict(map(reversed, a.items()))
# print(a_swapped)


# Task 14

a = {'a': 3, 'b': 2}
res = 0

for k, v in a.items():
    res += v

print(res)


# Task 15

a1 = {'x': 1, 'y': 2}
a2 = dict(x = 1, y = 1)
list_ = (('x', 1), ('y', 1))
a3 = dict(list_)


# Task 16

a = {'a': 10, 'b': 9, 'c': 3}
result = 1

for k, v in a.items():
    result *= v

print(result)


# Task 17

string = 'pythonist'

dict_ = {i: string.count(i) for i in string}
print(dict_)
