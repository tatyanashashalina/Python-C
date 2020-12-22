# Написать программу, которая позволяет пользователю ввести несколько строк с клавиатуры,
# а затем выводящую их в порядке возрастания длины строки

def increasedLenStr():
    str = " "
    lstStr = []
    print("Введите несколько строк с клавиатуры, для вывода их в порядке возрастания длины строки. "
          "После окончания ввода строк, для завершения, нажмите Enter")

    while True:
        str = input()
        if str != "":
            lstStr.append(str)
        else:
            break

    lstStr.sort(key=len)
    return lstStr

print(*increasedLenStr())


