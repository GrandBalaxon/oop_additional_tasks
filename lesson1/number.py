"""
Создай класс `Number` c полем `value` (указывается при инициализации)

Создай экземпляр, например `x = Number(7)`

Добавь методы:

`.get()` возвращает текущее value

`.add(<значение>)` добавляет указанное число к value

`.substract(<значение>)` вычитает указанное число из value
"""

class Number:
    value: int

    def __init__(self, value):
        self.value = value

    def get(self) -> int:
        return self.value

    def add(self, addend: int) -> int:
        self.value += addend
        return self.value

    def subtract(self, subtrahend: int) -> int:
        self.value -= subtrahend
        return self.value


if __name__ == '__main__':
    # код для проверки
    n = Number(7)
    print(n.get())  # 7
    n.add(3)
    print(n.get())  # 10
    n.subtract(5)
    print(n.get())  # 5
