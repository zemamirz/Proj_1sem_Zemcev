# Даны три целых числа: A, B, C. Проверить истинность высказывания: "Каждое из чисел A, B, C положительное".

a, b, c = input('Введите число a: '), input('Введите число b: '), input('Введите число c: ')  # ввод чисел

while type(a) != int:  # обработка исключений
    try:
        a = int(a)
    except ValueError:
        print('Некорректный ввод!')
        a = input('Введите число a: ')

while type(b) != int:  # обработка исключений
    try:
        b = int(b)
    except ValueError:
        print('Некорректный ввод!')
        b = input('Введите число b: ')

while type(c) != int:  # обработка исключений
    try:
        c = int(c)
    except ValueError:
        print('Некорректный ввод!')
        c = input('Введите число c: ')

print(bool((a > 0) and (b > 0) and (c > 0)))  # проверка на истинность: положительное или отрицательное
