# 5.Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int (input('Введите числа 0 или 1, X:'))
y = int (input('Введите число 0 или 1, Y:'))
z = int (input('Введите число 0 или 1, Z:'))
k = int
l = int
t = True
f = False

k == (not (x or y or z))
l == (not x and not y and not z)

if k == l:
    print(t)
else:
    print(f)
