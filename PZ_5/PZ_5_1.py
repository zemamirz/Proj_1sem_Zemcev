# Составить функцию, которая выполнит суммирования числового ряда


while True:
    try:  # обработка исключений
        len_row = int(input('Введите длину числового ряда: '))  # ввод целого числа
        break
    except ValueError:
        print("Некорректный ввод, попробуйте еще раз!")


def sum_num(len_row):  # функция суммирования
    res = 0
    i = 0
    n = 0
    while i < len_row:
        try:
            n += 1
            res += int(input(f'Введите {n} число: '))  # ввод n числа
            i += 1
        except ValueError:
            print("Некорректный ввод, попробуйте еще раз!")
    return res


print(f'Сумма числового ряда = {sum_num(len_row)}')  # вывод суммы числового ряда
