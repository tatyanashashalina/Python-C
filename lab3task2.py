# Написать программу, которая для введённой строки определяет количество слов и выводит каждое слово на отдельной
# строке и его длину

def countAndOutPrintWords():
    print("Для посчета количества слов введите строку.")
    counter = 0
    str = input()
    lstOut = str.split(" ")

    for word in lstOut:
        if word != "":
            counter += 1
            print(word, " - ", len(word))
    print("\nКоличество слов в строке: {}".format(counter))

countAndOutPrintWords()
