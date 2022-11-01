N = input('Введите число: ')  # ввод числа
K = 1
S = 1

while type(N) != int:  # обработчик исключений
    try:
        N = int(N)
    except ValueError:
        print('Неверный формат ввода')
        N = input('Введите число: ')

while S <= N:
    K += 1
    S += K
S -= K
K -= 1
print('Наибольшее целое число = {0}. Сумма = {1}'.format(K, S))  # вывод через формат
