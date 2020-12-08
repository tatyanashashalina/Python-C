# Написать программу, очищающую строку от лишних пробелов.Лишними считаются пробелы в начале строки,
# в конце строки и пробелы между словами, если их количество больше 1.

def delSpaces(str):
    lstStr = str.split(" ")
    print(lstStr)
    for word in range(len(lstStr)-1, -1, -1):
        if lstStr[word] == "":
            lstStr.pop(word)

    outStr = " ".join(lstStr)

    print(outStr)

delSpaces("  The tree   is    growing  .")
