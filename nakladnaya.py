""""
Создание класса Nakladnaya
"""
class Nakladnaya:
    # Метод инициализации
    def __init__(self, date, poluchatel, tovarov):
        self.date = date
        self.poluchatel = poluchatel
        self.tovarov = tovarov

    def __str__(self):
        return f"id: {self.date}, name: {self.poluchatel}, price: {self.tovarov}"
