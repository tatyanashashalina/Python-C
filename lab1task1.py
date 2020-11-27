# Написать программу, которая запрашивает у пользователя пол,  рост и вес, а затем анализирует соотношение роста и веса,
# выдавая рекомендации к дальнейшим действиям (похудеть, потолстеть, норма).

def getRecommendationBMI():
    print ("Для расчета ИМТ введите пол латинской буквой 'm' - мужской, 'w'  - женский, рост в см и вес в кг")
    gender = input()
    height = input()
    weight = input()

    if height.isdigit() == True and weight.isdigit() == True:
        if gender == "w":
            id_weight = int(height) - 110
        elif gender == "m":
            id_weight = int(height) - 100
        else:
            print("Введите корректное значение.")
    else:
        print("Введите числовые значения роста и веса.")
        return

    if int(weight) > id_weight:
        print ("Вес выше нормы.")
    elif int(weight) < id_weight:
        print ("Вес ниже нормы.")
    else:
        print("Вес в норме.")

getRecommendationBMI()
