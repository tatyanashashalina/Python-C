# Написать программу, которая читает построчно текстовый файл и переставляет случайно слова в каждой строке

import random

def mixRandomWordsInStr():

        with open('texts.txt', 'r+') as f:
            lstStr = f.read().split("\n")
            f.seek(0)
            for str in lstStr:
                lstWords = str.split(" ")
                random.shuffle(lstWords)
                outStr = " ".join(lstWords)
                f.write(outStr)
                f.write("\n")

mixRandomWordsInStr()
