n = int(input('Введите количество чисел в последовательности: '))

# Сразу же считаем сумму
sum = 0
for i in range(0, n):
    # Запрашиваем число
    input_value = int(input(f'Введите число #{i}: '))
    # Сразу же прибавляем его к сумме
    sum += input_value

print('Сумма всех чисел последовательности:', sum)
