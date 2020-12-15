# Написать программу, которая выводит на экран 10 паролей, сгенерированных случайным образом из латинских букв
# и цифр, причём буквы должны быть как в нижнем, так и в верхнем регистрах. Длина пароля - 8 символов

import string
import random

def randKey():
    lst = []
    for i in range(8):
        lst.append(random.choice(string.ascii_letters))
        lst.append(random.choice(string.digits))

    lstKey = random.choices(lst, k = 8)

    return lstKey

password = randKey()

def printPass():
    for i in range(10):
        print ("".join(randKey()))

printPass()
