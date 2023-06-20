# Создайте базовый класс "Транспорт" со свойствами "марка", "модель" и "год выпуска".
# От этого класса унаследуйте класс "Автомобиль" и добавьте в него свойство "тип кузова".
class Transport:
    def __init__(self, brand, model, release_date):
        self.brand = brand
        self.model = model
        self.release_date = release_date

    def __str__(self):
        return f'Марка: {self.brand}; Модель: {self.model}; Год выпуска: {self.release_date}'


class Automobile(Transport):
    def __init__(self, brand, model, release_date, k_type):
        super().__init__(brand, model, release_date)
        self.k_type = k_type

    def __str__(self):
        return f'Марка: {self.brand}; Модель: {self.model}; Год выпуска: {self.release_date}; Тип кузова: {self.k_type}'


trans = Transport('Porsche', 'Panamera', 2010)
car = Automobile('Lada', 'Priora', 1990, 'Sedan')
print(trans)
print(car)
