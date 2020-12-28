# Написать программу, переставляющую случайным образом символы каждого слова каждой строки текстового файла,
# кроме первого и последнего, то есть начало и конец слова меняться не должны

import random

def mixCharInWords():

    with open('text.txt', 'r') as f:
        lstStr = f.read().replace("\n", " ").split(" ")
        f.seek(0)

    with open('text.txt', 'w') as f:
        for word in lstStr:
            charLst = list(word)
            cutLst = charLst[1: len(charLst) - 1]
            random.shuffle(cutLst)
            charLst[1: len(charLst) - 1] = cutLst
            outWord = "".join(charLst)

            f.write(outWord)
            f.write("\n")

mixCharInWords()
