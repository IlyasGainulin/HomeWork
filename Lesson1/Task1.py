""" Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным. 
Пример: - 6 -> да - 7 -> да - 1 -> нет  """


def InputNumbers(inputText):
    its_OK = False
    while not its_OK:
        try:
            number = int(input(f"{inputText}"))
            its_OK = True
        except ValueError:
            print("Это не число!")
    return number


def checkNumber(num):
    if 6 <= num <= 7:
        print("Да")
    elif 0 < num < 6:
        print("нет")
    else:
        print("число вне пределов 7 дней")


num = InputNumbers("Введите число: ")
checkNumber(num)