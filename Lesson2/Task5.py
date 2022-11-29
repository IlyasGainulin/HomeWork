# Реализуйте алгоритм перемешивания списка.
def ignore(vodMas, count):
    n = 0
    while n in vodMas:
        n = random.randint(0, count*2-1)

    vodMas.append(n)
    return n


def shuffleMas(mas):
    ignoreMas = []
    count = int(len(mas)/2)
    # print(count)
    for i in range(count):
        first = ignore(ignoreMas, count)
        second = ignore(ignoreMas, count)
        swap = mas[first]
        mas[first] = mas[second]
        mas[second] = swap
    print(f"Перемешанный массив: {mas}")


a = ["1", "2", "3", "4", "5", "6"]

shuffleMas(a)
