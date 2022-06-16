# Task 1

list_ = [num for num in range(1, 101)]
print(list_)


# Task 2

list_ = [num for num in range(1, 51) if num % 2 != 0]
print(list_)


# Task 3

list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
int_list = [num for num in list_ if num % 2 == 0 and num > 0]
print(int_list)


# Task 4

list_ = [num ** 2 for num in range(1, 26)]
print(list_)


# Task 5

str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
int_list = [int(num) for num in str_list]
print(int_list)


# Task 6

list_ = [num if num % 2 != 0 else num ** 2 for num in range(1, 11)]
print(list_)


# Task 7

list_ = [num == num if num % 2 == 0 else num == False for num in range(1, 11)]
print(list_)


# Task 8

list_name = ['paul', 'john', 'george',
             'ringo', 'eric', 'patty', 
             'yoko', 'cynthia', 'linda', 
             'jude' ] 
new_list = [name.replace(name, 'shorter') if len(name) <= 4 else name.replace(name,'longer') for name in list_name]
print(new_list)


# Task 9

dict_ = {num: num ** 2 for num in range(1, 11)}
print(dict_)


# Task 10

n = int(input())
num = n
dict_ = {num: num ** 2 for num in range(1, 501) if num % n == 0}
print(dict_)


# Task 11

a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
dict_ = {k: list(range(1, v + 1)) for k, v in a.items()}
print(dict_)


# Task 12

dict_ = {'first': 1, 'second': 2, 'third': 3} 
a = {k: str(v).replace(f'{v}', 'even') if v % 2 == 0 else str(v).replace(f'{v}', 'odd') for k, v in dict_.items()}
print(a)


# Task 13

string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
splitted = string_.split()

list_ = [num for num in splitted if num.isdigit()]
print(list_)

# через цикл for
list_ = []
for num in splitted:
    if num.isdigit():
        list_.append(num)
print(list_)


# Task 14

dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91},
 
         'Olga': {'history': 92, 'math': 96, 'literature': 81},
 
         'Nik': {'history': 84, 'math': 85, 'literature': 87}
         }

list1 = []
for k in dict_.keys():
    list1.append(k)

list2 = []
for k, v in dict_.items():
    for inner_k in v.keys():
        if inner_k == max(v, key = v.get):
            list2.append(inner_k)  
new_dict = {list1[index]: list2[index] for index in range(len(list1))}

# new_dict = dict((list1[index] ,list2[index]) for index in range(len(list1)))
# new_dict = dict(zip(list1, list2))


print(new_dict)


# # неправильный вариант (на платформе выводит "результат верный")
# # если изменить значения, на выходе даст неправильный ответ
# list1 = []
# for k, v in dict_.items():
#     for inner_k in v.keys():
#         if inner_k == max(v, key = v.get):
#             list1.append(inner_k)  
# new_dict = {k: list1[0] if len(k) > 3 else list1[-1] 
#             for k in dict_.keys()}
# print(new_dict)


# Task 15

my_dict = {'first': {'a': 1}, 'second': {'b': 2}} 

list1 = []
for k, v in my_dict.items():
    list1.append(k)

list2 = []
for k, v in my_dict.items():
    for inner_k, inner_v in v.items():
        list2.append(inner_v)

dict_ = {list1[index]: list2[index] for index in range(len(list1))}
# dict_ = dict(zip(list1, list2))

print(dict_)


# Task 16

list_ = [num / 2 for num in range(0, 11) if num % 2 == 0]
print(list_)


# Task 17

# dict_ = {1: 'Hello', 2: 'World', 3: 'John'}
dict_ = {int(k): str(k) for k in range(1, 5)}
for k, v in dict_.items():
    if k % 2 == 0:
        dict_[k] = int(len(v))
    else:
        dict_[k] = int(len(v) ** 3)
print(dict_)


# Task 18

list1 = list(range(10))
list2 = list(range(8, 18))

set1 = {n1 for n1 in range(10)}
set2 = {n2 for n2 in range(8, 18)}

full_set = set1.union(set2)
length = len(list(full_set))

if length < 20:
    raznica = 20 - length
    print(f'В этом сете было {raznica} повторения, его длина составляет {length}')
else:
    print('Ваш объединенный сет полностью уникальный!')

