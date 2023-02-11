# 1. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# def fibonacci(num):
#     if num == 0:
#         fib = 0
#     elif num == 1:
#         fib = 1
#     else:
#         fib = fibonacci(num-1) + fibonacci(num-2)
#     return fib
#
# n = int(input("введите количество элементов: "))
# for i in range(n):
#     print(fibonacci(i))

# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.


# list_1 = []
# min_mark = list[0]
# max_mark = list[0]
# list_1 = [int(input(f'Введите оценку: ')) for _ in range(int(input('введите количество оценок: ')))] #list comrehension
# for i in list_1:
#     if i < min_mark:
#         min_mark = i
#     if i > max_mark:
#         max_mark = i
# print(min_mark, max_mark)
# print(list_1)
#
# for i in range(len(list_1)):
#     if list_1[i] == min_mark:
#         list_1[i] = max_mark
# print(list_1)

# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

number = int(input("Введите число: "))
def simpl_number(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if (num % i == 0):
            k = k + 1
    if (k <= 0):
        print("Число простое")
    else:
        print("Число не является простым")

simpl_number(number)
# решение на лекции
n = int(input())  # 20 -> 2, 4, 5, 10
for i in range(2, n // 2 + 1):
    if n % i == 0:
        print('Число не является простым')
        break
else:
    print('Простое')

n = int(input())  # 20 -> 2, 4, 5, 10
flag = False
for i in range(2, n // 2 + 1):
    if n % i == 0:
        print('Число не является простым')
        flag = True
        break
if not flag:
    print('Число простое')

#вариант через функцию
def simple(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return 'Число не является простым'
    return 'простое'

for i in range(1, 20):
    print(i, simple(i))




