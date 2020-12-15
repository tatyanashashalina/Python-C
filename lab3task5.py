# Написать программу, которая формирует целочисленный массив размера N, а затем находит сумму элементов,
# расположенным между первым отрицательным и последним положительным элементами

import random

def createRandLst():
    randNum = random.randint(15,20)
    lstNum = []

    for i in range(randNum):
        lstNum.append(random.randint(-10, 20))

    return lstNum

def sumNumOfLst(lst):
    print(lst)
    start = -1
    last = -1

    for i in range(len(lst)):
        if lst[i] < 0 and start == 0:
            start = i+1
        elif lst[i] >= 0:
            last = i

    if last > start:
        newLst = lst[start:last:1]
        print(newLst)
        print("Сумма элементов списка, расположенных между первым отрицательным и последним положительным элементами: {}.".
        format(sum(newLst)))
        return sum(newLst)

    else:
        print("Условия для подсчета суммы не выполнены.")

sumNumOfLst(createRandLst())
