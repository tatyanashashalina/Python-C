# Написать программу, переставляющую символы в массиве согласно правилу: сначала идут латинские буквы, потом цифры.
# Строка задается в коде программы в виде случайной последовательности букв ицифр.
# Пользоваться дополнительными массивами нельзя.
# Сортировка в данной задаче неприменима ввиду ее трудоемкости. Нужно использовать группировку элементов массива.
# Программа движется по строке с двух концов к середине и при встрече с нежелательными символами выполняет обмен
# с символом на другой стороне

import string
import random

def randMix():
    lst = []
    for i in range(100):
        lst.append(random.choice(string.ascii_letters))
        lst.append(random.choice(string.digits))

    lstChars = random.choices(lst, k = random.randint(5, 30))

    return lstChars

print(randMix)

lstCh = randMix()

def mySort(lst):
    i = 0
    j = len(lst)-1

    while i < j:
        if lst[i].isalpha() and lst[j].isalpha():
            i += 1
        elif lst[i].isdigit() and lst[j].isdigit():
            j -= 1
        elif lst[i].isdigit() and lst[j].isalpha():
            lst[i], lst[j] = lst[j], lst[i]
            i += 1
            j -= 1
        else:
            i += 1
            j -= 1

    print(lst)

mySort(lstCh)
