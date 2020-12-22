# Написать программу, сортирующую строки (см. задачу 1), но использующую строки, прочитанные из текстового файла.
# Результат работы программы также записывается в файл

def increasedLenStrFromFile():
    lstStr = []
    with open('text.txt', 'r') as f:
        for line in f:
            lstStr.append(line)

    outLst = [i.strip() for i in lstStr]
    outLst.sort(key=len)
    return outLst

print(*increasedLenStrFromFile())