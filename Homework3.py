# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
# пример
# 5
# 1 2 3 4 5
# 3
# -> 1
numbers = []
n = int(input("Введите количество элементов "))
x = int(input("Введите искомый элемент "))
for i in range(n):
    list.append(numbers, int(input()))
print(f"Колисечтво искомых элементов {numbers.count(x)}")


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# пример
# 5
# 1 2 3 4 5
# 6
# -> 5
#
numbers = []
n = int(input("Введите количество элементов: "))
mn = int()
for i in range(n):
    numbers.append(i + 1)
x = int(input("Введите искомый элемент "))
for i in range(n):
    if x <= 1:
        print("Максимально близкое значение = 1")
        break
    else:
        if numbers[i] == x:
            mn = numbers[i - 1]
            break
        if x > numbers[n - 1]:
            mn = numbers[n - 1]
print(f"Максимально близкое значение = {mn}")


# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.
# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
#
# пример
#
# Ввод:
# ноутбук
# Вывод:
# 12

points = {1:'AEIOULNSTRАВЕИНОРСТ',
      	2:'DGДКЛМПУ',
      	3:'BCMPБГЁЬЯ',
      	4:'FHVWYЙЫ',
      	5:'KЖЗХЦЧ',
      	8:'JZШЭЮ',
      	10:'QZФЩЪ'}

text = input("Введиет текст").upper()
print(sum([k for i in text for k, v in points.items() if i in v]))
