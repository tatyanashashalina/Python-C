# Написать программу, которая для введённой строки выводит самое длинное слово его длину

def choiceTheLenWord():
    print("Введите строку для определения самого длинного слова в ней.")
    str = input()
    lstWord= str.split(" ")
    length = 0
    theLenWord = ""

    for word in lstWord:
        if word != "" and len(word) > length:
            length = len(word)
            theLenWord = word
    print(theLenWord, " - ", len(theLenWord))

choiceTheLenWord()