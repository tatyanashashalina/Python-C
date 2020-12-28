# Написать программу, которая принимает от пользователя строку и выводит ее на экран,
# перемешав слова в случайном порядке

import random

def randWordsInStr():
    print("Введите строку для вывода слов из строки в рандомном порядке.")
    str = input()

    lstWords = str.split(" ")

    random.shuffle(lstWords)

    return lstWords

print(*randWordsInStr())
