# Организовать словарь на 10 англо-русских слов, обеспечивающий "перевод" английского слова на русский.

dic = {"Girl": "Девочка", "Boy": "Мальчик", "Food": "Еда", "Dog": "Собака", "Cat": "Кот",
       "Hello": "Привет", "Bye": "Пока", "Friend": "Друг", "Ball": "Мяч", "Horse": "Лошадь"} # Словарь
for key, value in dic.items():
    print(key, "(с англ.)", value)
write = input('Введите из предложенного списка слово на английском: ')
if write in dic:
    print(dic[write])
