# 1. Средствами языка Python сформировать текстовый файл (.txt), содержащий последовательность из целых
# положительных и отрицательных чисел.
# Сформировать новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую обработку элементов:
# Исходные данные:
# Количество элементов:
# Максимальный элемент:
# Среднее арифметическое элементов первой трети:

from random import randint

number = [randint(-100, 100) for i in range(10)]
numberThird = number[0:round(len(number) / 3)]

file1 = open('file_1.txt', 'w+', encoding='UTF-8')
file1.write(str(number))
file1.close()

file2 = open('file_2.txt', 'w+', encoding='UTF-8')
file2.write(f'Исходные данные: {number}\n')
file2.write(f'Количество элементов: {len(number)}\n')
file2.write(f'Максимальный элемент: {max(number)}\n')
file2.write(f'Среднее арифметическое элементов первой трети: {sum(numberThird) / len(numberThird)}')
file2.close()
