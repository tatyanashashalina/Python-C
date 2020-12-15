# Написать программу ”Угадай число”. Программа задумывает число в диапазоне от 1 до 100
# и пользователь должен угадать его за наименьшее количество попыток

import random

def guessNum():
    print("Программа задумала число в диапазоне от 1 до 100. Попробуйте угадать его за наименьшее количество попыток.")
    randNum = random.randint(1,100)
    attempt = 0
    print("Введите число.")

    while int(attempt) != randNum:
        attempt = input()

        if int(attempt) < 1 or int(attempt) > 100:
            print("Введеное число за пределами загадываемого диапазона. Попробуйте еще раз!")
        elif int(attempt) > randNum:
            print("Введеное число больше, чем загаданное. Попробуйте еще раз!")
        elif int(attempt) < randNum:
            print("Введеное число меньше, чем загаданное. Попробуйте еще раз!")
        else:
            print("Вы угадали!")

guessNum()
