# with open('les8test.txt', 'r', encoding='utf-8') as file:
    # text = file.read().splitlines()
    # print(text)
    # for el in text:
    #     print(el)
    # while True:
    #     line = file.readline()
    #     if not line:
    #         break
    #     print(line.strip())
# with open('filetest.txt', 'a', encoding='utf-8') as file:
#     some_list = ['привет', 'пока']
#     for word in some_list:
#         file.write(word + '\n')

# with open('les8test.txt', 'r', encoding='utf-8') as file:
#     letter = input("введите букву: ")
#     text = file.read()
#     counter = 0
#     for el in text:
#         if el == letter:
#             counter += 1
#     print(counter)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.




from random import randint
n = int(input('Введите кол-во элементов в списке: '))
some_list = [randint(-n, n) for _ in range(n)]
print(some_list)
with open('list.txt', 'w', encoding='utf-8') as file:
    for _ in range(randint(1, n)):
        file.write(str(randint(0, n - 1)) + '\n')

with open('list.txt', 'r', encoding='utf-8') as file:
    mult = 1
    for ind in file.read().splitlines():
        mult *= some_list[int(ind)]
print(mult)

