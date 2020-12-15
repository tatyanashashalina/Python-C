# Написать программу, подсчитывающую количество слов во введённой пользователем строке

def countWords():
    print("Для посчета количества слов введите строку.")
    str = input()
    counter = 0

    for ch in range(len(str)):
        if (str[ch - 1]  == " " or str[ch - 1] == "") and str[ch] != " ":
            counter += 1
    return counter

print ("Количество слов в строке: {}".format(countWords()))
