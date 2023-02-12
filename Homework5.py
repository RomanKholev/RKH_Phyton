# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
# num = int(input("Введите число: "))
# pwr = int(input("Введите степень: "))
# def num_power(num, pwr):
#     if pwr == 1:
#         res = num
#     else:
#         res = num * num_power(num, pwr-1)
#     return res
# print(f"{num}^{pwr}={num_power(num, pwr)}")

# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# 2 2
# 4
num1 = int(input("Веедите первое число: "))
num2 = int(input("Веедите второе число: "))
def summa(a, b):
    if a < b:
        tmp = a
        a = b
        b = tmp
    if b > 0:
        res = summa(a + 1, b -1)
    else:
        res = a
    return res
print(f"{num1}+{num2}={summa(num1, num2)}")