# Задача 2: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = input("Введите трехзначное число: ")
while len(a) != 3:
    print("Введенное число не трехзначное")
    a = (input("Введите трехзначное число: "))
a = int(a)
print(f'Сумма цифр {a // 100 , a // 10 % 10 , a % 10} = {a // 100 + a // 10 % 10 + a % 10}')

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

s = int(input("Ввведите колличество журавликов: "))
while s % 6 !=0:
    print("Следуя из уcловий задачи число сделанных журавликов должно быть кратно 6")
    s = int(input("Ввведите колличество журавликов кратное 6: "))
print(f'Петя и сережа сделали по: {int(s / 6)}, Катя сделала: {int(s / 6 * 4)}')

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# 385916 -> yes
# 123456 -> no

n = input("Введите шестизначное число: ")
while len(n) != 6:
    print("Введенное число не шестизначное")
    n = (input("Введите шестизначное число: "))
n=int(n)
n1 = (n//1000)
n2 = n - n1*1000
summa_n1 = n1 // 100 + n1 // 10 % 10 + n1 % 10
summa_n2 = n2 // 100 + n2 // 10 % 10 + n2 % 10
if summa_n1 == summa_n2:
    print("YAS")
else:
    print("NO")

# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input("Введите сторону N шоколадки: "))
m = int(input("Введите сторону M шоколадки: "))
k = int(input("Введите количество долек: "))
if k < n * m and k % n == 0 or k % m == 0:
    print("Yas")
else:
    print("NO")


