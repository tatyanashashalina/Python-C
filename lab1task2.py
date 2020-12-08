# Написать программу, которая запрашивает текущее время в формате ЧЧ:ММ:СС, а затем выводит приветствие
# в зависимости от указанного времени("Доброе утро", Добрый день" и т.д.)

def progammGreeting():
    print ("Введите время в формате ЧЧ:ММ:СС.")
    str_curr_time = input()
    lst = str_curr_time.split(":")

    try:
        if int(lst[0]) >= 4 and int(lst[0]) < 12:
            print ("Доброе утро")
        elif int(lst[0]) >= 12 and int(lst[0]) < 18:
            print("Добрый день")
        elif int(lst[0]) >= 18 and int(lst[0]) < 21:
            print("Добрый вечер")
        elif int(lst[0]) >= 22 and int(lst[0]) < 24 or int(lst[0]) >= 0 and int(lst[0]) < 4:
            print("Добрая ночь")
        else:
            print("Введите корректное значение")

    except ValueError:
        print("Введите корректное значание.")

progammGreeting()
