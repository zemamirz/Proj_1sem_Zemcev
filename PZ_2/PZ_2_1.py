# Дано двузначное число. Найти сумму и произведение его цифр.

try:  # обработчик исключений
    num = int(input("Введите двузначное число:"))  # Ввод числа
    a = num // 10  # Нахождение первой цифры
    b = num % 10  # Нахождение второй цифры
    c = a * b  # Нахождение произведения цифр
    d = a + b  # Нахождение суммы цифр
    print("Произведение цифр этого числа равно", c, ".", "Сумма цифр этого числа равна", d,
          ".")  # Вывод произведения и суммы
except:
    print('Error!!!')  # Вывод ошибки
