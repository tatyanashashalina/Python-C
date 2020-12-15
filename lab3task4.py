# Написать программу, которая находит сумму чисел во введённой строке

import re

def sumNum():
    print("Введите строку для которой необходимо найти сумму чисел.")
    strCh = input()
    sum = 0

    lstNum = re.findall("\d*", strCh)
    for num in lstNum:
        if num.isdigit():
            sum = sum + int(num)

    return sum


print("Сумма чисел во введеной строке равна {}.".format(sumNum()))