# Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно последние строки в количестве lines
# (на всякий случай проверим, что задано положительное целое число). Протестируем функцию на файле «article.txt» со следующим содержимым:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
def read_last(lines, file):
    if lines > 0:
        with open(file, encoding='utf-8') as text:
            text = text.readlines()[-lines:]
        for line in text:
            print(line.strip())
    else:
        print('Количество строк может быть только целым положительным')
line = int(input('введите количество строк: '))
read_last(line, "article.txt")


# Документ «article.txt» содержит следующий текст:
# Вечерело
# Жужжали мухи
# Светил фонарик
# Кипела вода в чайнике
# Венера зажглась на небе
# Деревья шумели
# Тучи разошлись
# Листва зеленела
#
# Требуется реализовать функцию longest_words(file), которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько).
def longest_words(file):
    with open(file, encoding='utf-8') as text:
        text = text.read().split()
        max_length = len(max(text, key=len))
        words = [word for word in text if len(word) == max_length]
        return words

print(longest_words('article.txt'))