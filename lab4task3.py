# Написать программу, которая запрашивает строку и определяет, не является ли строка палиндромом
# (одинаково читается и слева направо и справа налево)

def isPali(str):
    lst = str.split(" ")
    newStr = "".join(lst)
    reverseStr = newStr[::-1]

    if reverseStr == newStr:
        print("Строка является палиндромом.")
    else:
        print("Строка не является палиндромом.")

isPali("non")