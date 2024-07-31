class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        elif isinstance(other, int):
            return self.floors == other
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        elif isinstance(other, int):
            return self.floors < other
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        elif isinstance(other, int):
            return self.floors <= other
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        elif isinstance(other, int):
            return self.floors > other
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        elif isinstance(other, int):
            return self.floors >= other
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, House):
            return self.floors != other.floors
        elif isinstance(other, int):
            return self.floors != other
        else:
            return NotImplemented

    def __add__(self, value):
        if isinstance(value, int):
            return House(self.name, self.floors + value)
        else:
            return NotImplemented

    __radd__ = __add__
    __iadd__ = __add__

# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # eq

h1 = h1 + 10  # add
print(h1)
print(h1 == h2)

h1 += 10  # iadd
print(h1)

h2 = 10 + h2  # radd
print(h2)

print(h1 > h2)  # gt
print(h1 >= h2)  # ge
print(h1 < h2)  # lt
print(h1 <= h2)  # le
print(h1 != h2)  # ne