# Написать программу, которая формирует целочисленный массив размера N, а затем находит сумму элементов между
# первым минимальным и первым максимальным элементами


import random

def createRandLst():
    randNum = random.randint(10,15)
    lstNum = []

    for i in range(randNum):
        lstNum.append(random.randint(-10, 20))

    return lstNum

def sumMinMaxOfLst(lst):
    print(lst)
    minNum = 0
    maxNum = 0
    minIndex = 0
    maxIndex = 0

    for i in range(len(lst)):
        if lst[i] < minNum:
            minNum = lst[i]
            minIndex = i
        elif lst[i] > maxNum:
            maxNum = lst[i]
            maxIndex = i

    if maxIndex > minIndex:
        newLst = lst[minIndex+1:maxIndex:1]
        print(newLst)
        print("Сумма элементов списка, расположенных между первым минимальным и первым максимальным элементами {}.".
            format(sum(newLst)))
        return sum(newLst)

    elif minIndex > maxIndex:
        newLst = lst[maxIndex+12:minIndex:1]
        print(newLst)
        print("Сумма элементов списка, расположенных между первым минимальным и первым максимальным элементами {}.".
            format(sum(newLst)))
        return sum(newLst)

    else:
        print("Условия для подсчета суммы не выполнены.")

sumMinMaxOfLst(createRandLst())
