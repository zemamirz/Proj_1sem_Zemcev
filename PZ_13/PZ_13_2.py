# В матрице найти отрицательные элементы, сформировать из них новый массив. Вывести размер полученного массива.

from random import randint

matrix = [[randint(-5, 5) for j in range(3)] for i in range(3)]

negative = [elem for row in matrix for elem in row if elem < 0]
print('Вывод матрицы 3х3: ')
for i in matrix:
    print(i)

print('Длина списка отрицательных элементов: ', len(negative))
print(f'Список отрицательных элементов: {negative}')
