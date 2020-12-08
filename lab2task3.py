# Написать программу, выводящую на экран треугольник из звёздочек. Треугольник должен выглядеть так:
#    *
#   ***
#  *****
##*******
# Количество строк задаётся пользователем с клавиатуры.

def triangleDraw():
    print("Для вывода на экран треугольника из звёздочек задайте необходимое количество строк.")
    numStr = int(input())
    numStars = 1
    outStr = ""

    for i in range(numStr):
        numSpaces = numStr - i - 1

        outStr += " " * (numSpaces)
        outStr += "*" * (numStars)

        # for space in range(numSpaces):
        #     outStr += " "
        # for star in range(numStars):
        #     outStr += "*"

        print(outStr)
        numStars += 2
        outStr = ""

triangleDraw()
