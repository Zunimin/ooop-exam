from datetime import datetime
from item import *
from nakladnaya import *



item1 = Item(1, "Яблоки", 50)
item2 = Item(2, "Бананы", 30)
nakladnaya = Nakladnaya(
    datetime.now(),
    "ООО Фрукты",
    {item1: 10, item2: 5}
)

nakladnaya.tovarov[item1] = 15

with open('nakladnaya.csv', 'w', encoding='utf-8') as f:
    f.write('data;poluchatel;tovar;kolvo\n')
    f.write(f"{nakladnaya.date.strftime('%d.%m.%Y')};{nakladnaya.poluchatel};Яблоки;15\n")
    f.write(f"{nakladnaya.date.strftime('%d.%m.%Y')};{nakladnaya.poluchatel};Бананы;5\n")

print("Сохранено в файл nakladnaya.csv")
