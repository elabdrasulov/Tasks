# Task 1

number = int(input())
if number > 0:
    print(True)
else:
    print(False)


# Task 2

string = input()
length = int(len(string))

if length > 5:
    print(True)
else:
    print(False)


# Task 3

mark = int(input())

if mark >= 90:
    print('Отлично, Ваша оценка 5!')
elif mark >= 80:
    print('Здорово, Ваша оценка 4!')
elif mark >= 70:
    print('Хорошо, Ваша оценка 3!')
elif mark >= 60:
    print('Вам стоит подучить материал')
else:
    print('Вы не сдали экзамен')


# Task 4

number = int(input())

if number == -abs(number) and number != 0:
    print('negative')
elif number == abs(number) and number !=0:
    print('positive')
else:
    print('zero')


# Task 5

x = 2
y = 1

if x < y:
    print(x)
else:
    print(y) 


# Task 6

x = 1
y = 10
z = 3

if y < z and y < x:
    print(y) 
elif x < y and x < z:
    print(x)
else:
    print(z)


# Task 7

x = 1
y = 2
z = 3

if x == y and y == z:
    print(3)
elif x == y or y == z:
    print(2)
else:
    print(0)


# Task 8

x = int(input())
y = int(input())

division = x // y
division1 = x / y
modulo = x % y

if division < division1:
    print(f'x не делится на y\nЧастное: {division}\nОстаток: {modulo}')
else:
    print(f'x делится на y\nЧастное: {division}')


# Task 9

year = int(input())

if year / 4 == year // 4 and year / 100 > year // 100:
    print('YES')
else:
    print('NO')


# Task 10

nums = [3, 9, 86, 99]
target = 10

if target in nums:
    print('Да')
else:
    print('Нет')


# Task 11

num = int(input())

if num > 64 and num < 91: # верхние регистры A-Z
    print(f'Это буква \"{chr(num)}\"')
elif num > 96 and num < 123: # нижние регистры a-z
    print(f'Это буква \"{chr(num)}\"')
else:
    print(f'Это не буква, а символ \"{chr(num)}\"')    


# Task 12

greeting = input()

if greeting == 'Hi':
    print("Привет!")
else:
    print("NO")


# Task 13

count = 0
number = input()

if number.isdigit():
    number = int(number)
else:
    number = 0

count = number
print(count)

