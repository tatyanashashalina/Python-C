# Написать программу, которая запрашивает у пользователя пол,  рост и вес, а затем анализирует соотношение роста и веса,
# выдавая рекомендации к дальнейшим действиям (похудеть, потолстеть, норма)

def getRecommendationBMI():
    print ("Для расчета ИМТ введите пол латинской буквой 'm' - мужской, 'w'  - женский, рост в см и вес в кг")
    gender = int(input())
    height = int(input())
    weight = int(input())

    if height.isdigit() and weight.isdigit():
        if gender == "w":
            id_weight = height - 110
        elif gender == "m":
            id_weight = height - 100
        else:
            print("Введите корректное значение.")
            return
    else:
        print("Введите числовые значения роста и веса.")
        return

    if weight > id_weight:
        print ("Вес выше нормы.")
    elif weight < id_weight:
        print ("Вес ниже нормы.")
    else:
        print("Вес в норме.")

getRecommendationBMI()
