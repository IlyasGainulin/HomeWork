# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
# with open("file.txt", "r") as f:
#     firstIndex = int(f.readline())
#     secondIndex = int(f.readline())


def collection(n):
    result24 = []
    for i in range(-n, n+1):
        result24.append(i)
    print(result24)
    mult = result24[firstIndex]*result24[secondIndex]
    print(mult)
