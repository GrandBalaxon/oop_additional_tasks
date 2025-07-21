"""
Напишите класс Fraction, представляющий собой дробь, имеющий следующие методы:

- __init__(self, numerator, denominator): конструктор, принимающий числитель и знаменатель дроби;
- __repr__(self): магический метод, возвращающий строковое представление дроби,
которое можно использовать для создания нового объекта класса Fraction;
- __str__(self): магический метод, возвращающий строковое представление дроби;
- __add__(self, other): магический метод, который позволяет складывать дроби и возвращать новую дробь.
"""


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return f"Fraction({self.numerator}, {self.denominator})"

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other: "Fraction"):
        if self.denominator >= other.denominator:
            x_nu, x_de = self.numerator, self.denominator
            y_nu, y_de = other.numerator, other.denominator
        else:
            y_nu, y_de = self.numerator, self.denominator
            x_nu, x_de = other.numerator, other.denominator

        if x_de == y_de:
            pass
        elif x_de % y_de == 0: # если он больше в n-разiв
            multiplier = x_de // y_de
            y_nu = y_nu * multiplier
        else: # если больше, но сложно 18 и 5
            x_nu, y_nu, x_de = x_nu * y_de, y_nu * x_de, x_de * y_de

        new_numerator = x_nu + y_nu
        new_denominator = x_de

        while True:
            lesser_num = new_numerator if new_numerator < new_denominator else new_denominator
            biggest_denominator = 0

            for i in range(2, lesser_num + 1):
                if not (new_numerator % i) and not (new_denominator % i):
                    biggest_denominator = i

            if biggest_denominator:
                new_numerator = round(new_numerator / biggest_denominator)
                new_denominator = round(new_denominator / biggest_denominator)
            else:
                break

        return Fraction(new_numerator, new_denominator)


if __name__ == '__main__':
    # код для проверки
    fraction1 = Fraction(3, 6)
    print(repr(fraction1))  # Fraction(3, 6)
    print(str(fraction1))  # 3/6

    fraction2 = Fraction(2, 14)
    fraction3 = fraction1 + fraction2
    print(fraction3)  # 9/14
