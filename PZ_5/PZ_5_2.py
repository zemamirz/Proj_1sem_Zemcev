# Описать функцию SortDec(A,B,C), меняющую содержимое переменных A, B, C таким образом, чтобы их значения оказались
# упорядоченными по убыванию (A, B, C - вещественные параметры, являющиеся одновременно входными и выходными). С помощью
# этой функции упорядочить по убыванию два данных набора из трёх чисел: (A1, B1, C1) и (A2, B2, C2)

def SortDec3(A: float, B: float, C: float):  # функция сортировки по убыванию
    if A < C:
        A, C = C, A  # меняем местами a и c
    if A < B:
        A, B = B, A  # меняем местами a и b
    if B < C:
        B, C = C, B  # меняем местами b и c
    return A, B, C  # возвращаем a, b, c


A1, B1, C1 = input('Введите первый набор чисел\nВведите A1: '), input('Введите B1: '), input('Введите C1: ')
A2, B2, C2 = input('Введите второй набор чисел\nВведите A2: '), input('Введите B2: '), input('Введите C2: ')  # ввод
# вещественного числа

while type(A1) != float or type(B1) != float or type(C1) != float:  # обработка исключений
    if type(A1) != float:
        try:
            A1 = float(A1)
        except ValueError:
            print('Некорректный ввод!')
            A1 = input("Введите число A1: ")

    if type(B1) != float:
        try:
            B1 = float(B1)
        except ValueError:
            print('Некорректный ввод!')
            B1 = input("Введите число B1: ")

    if type(C1) != float:
        try:
            C1 = float(C1)
        except ValueError:
            print('Некорректный ввод!')
            C1 = input("Введите число C1: ")

while type(A2) != float or type(B2) != float or type(C2) != float:  # обработка исключений
    if type(A2) != float:
        try:
            A2 = float(A2)
        except ValueError:
            print('Некорректный ввод!')
            A2 = input("Введите число A2: ")

    if type(B2) != float:
        try:
            B2 = float(B2)
        except ValueError:
            print('Некорректный ввод!')
            B2 = input("Введите число B2: ")

    if type(C2) != float:
        try:
            C2 = float(C2)
        except ValueError:
            print('Некорректный ввод!')
            C2 = input("Введите число C2: ")

print(f'Первый набор чисел: {SortDec3(A1, B1, C1)}')  # вывод по убыванию первого набора чисел
print(f'Второй набор чисел: {SortDec3(A2, B2, C2)}')  # вывод по убыванию второго набора чисел
