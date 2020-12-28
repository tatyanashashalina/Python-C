# Написать программу, подсчитывающую количество слов во введённой пользователем строке

def countWords():
    print("Для посчета количества слов введите строку.")
    str = input()
    lst = str.split(" ")
    counter = 0

    for word in lst:
        if word != "":
            counter += 1
    return counter

print ("Количество слов в строке: {}".format(countWords()))
