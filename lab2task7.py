# Написать программу, выводящую таблицу встречаемости символов для введенной пользователем строки.
# В этой таблице содержится символ строки и число его повторений

def frequency(str):
    lst = list(str)
    print(lst)
    dict = {}

    for elem in lst:
        if elem in dict:
            dict [elem] += 1
        else:
            dict[elem] = 1

    lstKeys = list(dict.keys())
    lstKeys.sort()

    for i in lstKeys:
        print(i, " : ", dict[i])

frequency("bbbbbbccccdddddaaaaaaaaa")
