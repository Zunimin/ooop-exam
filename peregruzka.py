a = 10
b = 5
print(f"Числа: {a} + {b} = {a + b}")

s1 = "Hello"
s2 = "World"
print(f"Строки: '{s1}' + '{s2}' = '{s1 + s2}'")


list1 = [1, 2]
list2 = [3, 4]
print(f"Списки: {list1} + {list2} = {list1 + list2}")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(f"Векторы: {v1} + {v2} = {v1 + v2}")
