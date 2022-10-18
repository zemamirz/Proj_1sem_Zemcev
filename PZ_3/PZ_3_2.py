try:
    a = int(input('Введите число: ')) #
    if a > 0: #
        print ('Положительное') #
    else: #
        print ('Отрицательное') #
    if a % 2 == 0: #
        print ('Чётное') #
    else: #
        print ('Нечётное') #
    if a == 0: #
        print ('Нулевое число') #
except:
    print('Неверный ввод') #