# Написать программу ”Калейдоскоп”, выводящую на экран изображение, составленное из симметрично расположенных звездочек
# ’*’. Изображение формируется в двумерном символьном массиве, в одной его части и симметрично копируется в остальные
# его части.

import random

def kaleidoscope():
    width = 7
    height = 6

    lst = []
    for i in range(height):
        lst.append([])
        for j in range(width):
            if random.randint(0,1):
                lst[i].append("*")
            else:
                lst[i].append(" ")

    for i in range(len(lst)-1,-1,-1):
        lst.append(lst[i])
        for j in range(len(lst[i])-1,-1,-1):
            lst[i].append(lst[i][j])

    for i in lst:
        print(*i)

kaleidoscope()
