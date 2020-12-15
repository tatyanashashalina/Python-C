# Написать программу, которая печатает таблицу встречаемости символов для введённой строки,
# отсортированную по убыванию частоты

def frequency():
    print("Для создания таблицы встречаемости символов введите строку.")
    str = input()
    dict = {}
    for ch in str:
        if ch in dict:
            dict[ch] +=1
        else:
            dict[ch] = 1

    lstVal = list(dict.items())
    lstVal.sort(key=lambda i : i[1])

    for i in lstVal:
        print(i[0], ':', i[1])

frequency()
