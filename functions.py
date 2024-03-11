#
# def func(x):
#     return x+1
#
#
# class TestCases:
#     def test_1(self):
#         assert func(3) == 4
#
#     def test_2(self):
#         assert func(4) == 6
#
#     def test_3(self):
#         assert func(5) == 6
#
#     def test_4(self):
#         print()

import math
import requests


def add(number_one, number_two):
    return number_one + number_two


def divide(number_one, number_two):
    if number_two == 0:
        raise ValueError
    return number_one / number_two


class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print(math.pi * self.radius ** 2)
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __eq__(self, other):
        # built-in function used for type checking
        if not isinstance(other, Rectangle):
            return False

        return (self.width == other.width) and (self.length == other.length)

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (self.length * 2) + (self.width * 2)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __eq__(self, other):
#         return self.name == other.name and self.age == other.age
#
#
# x = Person('Mike', 25)
# y = Person('Sarah', 27)
# z = Person('Mike', 25)
#
# print("Confirm: ", x == z)


datasource = {
    1: "apple",
    2: "banana",
    3: "mango"
}


def retrieve_fruit(fruitid):
    return datasource.get(fruitid)


def get_users():
    response = requests.get("https://jsonplaceholder.typicode.com/users")

    if response.status_code == 200:
        return response.json()

    raise requests.HTTPError


class StudentsLimit(Exception):
    pass


class Classroom:
    def __init__(self, teacher, students, course):
        self.teacher = teacher
        self.students = students
        self.course = course

    def add_student(self, student):
        if len(self.students) <= 10:
            self.students.append(student)
        else:
            raise StudentsLimit

    def remove_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                break

    def change_teacher(self, new_teacher):
        self.teacher = new_teacher


class Person:
    def __init__(self, name):
        self.name = name


class Teacher(Person):
    pass


class Student(Person):
    pass
