# Написать программу, которая переводит рост из американской системы (футы, дюймы) в европейскую (сантиметры).
# Данные вводятся в виде двух целых чисел, выводятся в виде вещественного числа с точностью до 1 знака.
# 1 фут = 12 дюймов. 1 дюйм = 2.54 см.

def int_r(num):
    num = round(num*10 + (0.05 if num*10 > 0 else -0.05))
    return num/10

def changeHeightUnit():
    valFoot = 12*2.54
    valInch = 2.54
    bul = 0


    print("Для перевода в метрическую систкму ввведите целое количество футов роста.")
    heightValFoot = input()
    print("Введите количество дюймов.")
    heightValInch = input()

    try:
        heightVal = int(heightValFoot)*valFoot + int(heightValInch)*valInch
        print("Ваш рост в метрической системе - ",  int_r(heightVal), "см." )

    except ValueError:
        bul = 1
        print("Введите корректное значание.")
        while bul == 1:
            changeHeightUnit()
            bul = 0

changeHeightUnit()
