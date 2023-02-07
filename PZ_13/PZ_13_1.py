# В матрице найти сумму и произведение элементов столбца N (N задать с клавиатуры).

from random import randint


def sum_mult(col, matr):
    summa = 0
    mult = 1
    for i in matr:
        summa += i[col - 1]
        mult *= i[col - 1]
    return summa, mult


matrix = [[randint(-5, 5) for j in range(5)] for i in range(5)]

print('Вывод матрицы 5x5: ')
for i in matrix:
    print(i)

column = int(input('Введите номер столбца, сумму м произведение которого вы хотите найти (1-5): '))
summ, mult = sum_mult(column, matrix)

if 1 <= column <= len(matrix):
    print(f'Выбранный столбец: {column} \nЕго сумма = {summ}, а произведение = {mult}')
else:
    print('Недопустимое значение')
