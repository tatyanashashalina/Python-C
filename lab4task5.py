# Написать программу, которая запрашивает количество родственников в семье, а потом позволяет ввести имя родственника
# и его возраст. Программа должна определить самого молодого и самого старого родственника и вывести их имена

def ageComparison():
    print("Введите количество родственников в семье. Затем введите имя родственника и его возраст, "
          "чтобы определить самого молодого и самого старого родственника и вывести их имена."
          "Для завершения ввода нажмите два раза Enter.")

    relatives = {}

    while True:
        print("Введите имя родственника.")
        rel = input()
        if rel != "":
            print("Введите возраст родственника.")
            try:
                age = int(input())

            except ValueError:
                ("Введите корректное значение.")

            if not rel in relatives:
                relatives[rel] = age

        else:
            break

    if not relatives:
        print("Данные не были заполнены. Повторите заполнение.")

    else:
        lstRel = list(relatives.items())
        lstRel.sort(key=lambda i : i[1])

        print(lstRel[0][0], " : ", lstRel[0][1])
        print(lstRel[len(lstRel)-1][0], " : ", lstRel[len(lstRel)-1][1])

ageComparison()
