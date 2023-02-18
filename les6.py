# 39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве.
# Пользователь вводит число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве.
# Затем элементы второго массива
# n = int(input("Введите количество элементов первого массива: "))
# array_1 = [int(input(f'Введите {i + 1} элемент первого множества: ')) for i in range(n)]
# m = int(input("Введите количество элементов первого множества: "))
# array_2 = [int(input(f'Введите {i + 1} элемент второго массива: ')) for i in range(m)]
# array_2_set = set(array_2)
# for el  in array_1:
#     if el not in array_2_set:
#         print(el)


#41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала вводится число N — количество элементов в массиве
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.

# list = [int(input()) for _ in range(int(input("Введитк количество чисел: ")))]
# count = 0
# for ind in range(1, len(list) -1):
#     if list[ind-1] < list[ind] > list[ind + 1]:
#         count += 1
# print(count)

# 43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел пока не введут 0. Все числа списка находятся на разных строках.

# list = []
# while True:
#     number = int(input())
#     if number == 0:
#         break
#     list.append((number))
#
# count_dict = {}
#
# for el in list:
#     if count_dict.get(el):
#         count_dict[el] += 1
#     else:
#         count_dict[el] = 1
# count = 0
# for value in count_dict.values():
#     count += value // 2
# print(count)


# 45. Два различных натуральных числа n и m называются дружественными,
# если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k.
# Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k.
# Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

def sum_div(n):
    summa = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            summa += i
    return summa

summ_dict = {}

k = int(input())
for number in range(1, k + 1):
    if number in summ_dict:
        if sum_div(number) == summ_dict[number]:
            print(number, summ_dict[number])
    summ_dict[sum_div(number)] = number
