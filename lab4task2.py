# Написать программу, которая с помощью массива указателей выводит слова строки в обратном порядке.
# Пример: "буря мглою небо кроет" -> "кроет небо мглою буря"

def reverseWord(str):
    lst = str.split(" ")
    lst.reverse()
    return lst

print(*reverseWord("буря мглою небо кроет"))