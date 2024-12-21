import pymorphy2

# Файл NOUNS_5букв.txt должен находится в одной папке с этим файлом
filename: str = "NOUNS_5букв.txt"
morph = pymorphy2.analyzer

# Открываем файл в список слов
with open(filename, encoding="utf8") as file:
    lines: list = [line.rstrip() for line in file]
print(len(lines))
lst: list = []
lst1: list = []

# Нужно ввести буквы. В кортежи позиции где МОЖЕТ стоять буква
loc_word: dict = {"т": (0,2,), "с": (1, 4,)}

# Буквы которых нет в слове
notword: list = ["е", "н", "а", "к", "и", "ь", "х", "в", "в", "в", "в"]

# Проходим по списку слов
for word in lines:

    # Если слово с большой буквы, то пропускаем
    if word[0].isupper():
        continue

    # Проходим по словарю с буквами
    for letter in loc_word:

        # Проверяем есть ли буква в слове
        if word.find(letter) == -1:
            lst1 = []
            break

        # Проходим по возможным позициям
        if word.find(letter) not in loc_word[letter]:
            lst1 = []
            break
        else:
            # Есть ли буквы которых не должно быть
            if set(word) & set(notword):
                continue
            if word not in lst1:
                lst1.append(word)
    # Добвляем слово в список если его там нет
    lst.extend([item for item in lst1 if item not in lst])

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(len(lst))
    print(lst)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
