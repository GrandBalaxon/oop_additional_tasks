"""
Создай класс Student (студент) с полями

- Имя (name) - строка
- Курс (course) - целое число

Создай два экземпляра

- Алиса , 3 [курс]
- Маргарита , 2 [курс]
"""


class Student:
    name: str
    course: int

    def __init__(self, name, course):
        self.name = name
        self.course = course


student_1 = Student("Алиса", 3)
student_2 = Student("Маргарита", 2)


if __name__ == '__main__':
    # код для проверки
    print(student_1.name, student_1.course)  # Алиса 3
    print(student_2.name, student_2.course)  # Маргарита 2
