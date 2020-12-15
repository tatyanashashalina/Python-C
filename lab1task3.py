# Написать программу, которая переводит значение угла из градусов в радианы, и, наоборот, в зависимости от символа
# при вводе.Например: 45.00D - означает значение в градусах, а 45.00R - в радианах

import math

def changeCornerUnit():
    print("Введите значение угла для перевода из градусов в радианы, и наоборот.")
    str = input()

    try:
        num = float(str[0:len(str)-1])

        if str[len(str)-1] == "D":
            val = (num * math.pi) / 180
            print(val)

        elif str[len(str)-1] == "R":
            val = (num * 180) / math.pi
            print(val)

        else:
            print("Введите корректное значение")

    except ValueError:
        print("Введите переводимое значание с корректным разделителем - '.'.")

changeCornerUnit()
