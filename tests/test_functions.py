import time
import math

import pytest
import requests

import functions as instance_test_demo
import unittest.mock as mock

from functions import Classroom, Student, Teacher

# def test_add():
#     sumofnumbers = instance_test_demo.add(2, 6)
#     assert sumofnumbers == 8
#
#
# def test_divide():
#     quotientofnumbers = instance_test_demo.divide(20, 10)
#     assert quotientofnumbers == 2
#
#
# def test_divide_by_zero():
#     with pytest.raises(ValueError):
#         instance_test_demo.divide(20, 0)
#
#
# def test_concat_string():
#     concatenated = instance_test_demo.add("first word", "second word")
#     assert concatenated == "first wordsecond word"


class TestCircle:

    def setup_method(self, method):
        print(f"--Setting up-- {method}")
        self.circle = instance_test_demo.Circle(10)

    def teardown_method(self, method):
        print(f"--Tearing down-- {method}")
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2
        print(self.circle.area())

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * math.pi * self.circle.radius
        assert result == expected

    def test_not_same_area_rectable(self, correct_rectangle):
        assert self.circle.area() != correct_rectangle.area()


#
#     def test_one(self):
#         assert True
#
#     def test_two(self):
#         assert True

# def test_area():
#     rectangle = instance_test_demo.Rectangle(10, 20)
#     assert rectangle.area() == 10 * 20
#
#
# def test_perimeter():
#     rectangle = instance_test_demo.Rectangle(10, 20)
#     assert rectangle.perimeter() == (10 * 2) + (20 * 2)

#  --change to--


def test_area(correct_rectangle):
    assert correct_rectangle.area() == 10 * 20


def test_perimeter(correct_rectangle):
    assert correct_rectangle.perimeter() == (10 * 2) + (20 * 2)


def test_not_equal(correct_rectangle, improper_rectangle):
    assert correct_rectangle != improper_rectangle


@pytest.mark.slow
def test_time_slow():
    time.sleep(5)
    quotientofnumbers = instance_test_demo.divide(20, 10)
    assert quotientofnumbers == 2


@pytest.mark.skip(reason="Feature under construction")
def test_add():
    assert instance_test_demo.add(1, 2) == 3


@pytest.mark.xfail(reason="Division by zero is not allowed")
def test_division_by_zero():
    assert instance_test_demo.divide(4, 0)


@pytest.mark.parametrize("side, expected_area", [(5, 25), (4, 16), (9, 81)])
def test_multiple_square_area(side, expected_area):
    assert instance_test_demo.Square(side).area() == expected_area


@pytest.mark.parametrize("side, expected_perimeter", [(3, 12), (4, 16), (5, 20)])
def test_multiple_square_perimeters(side, expected_perimeter):
    assert instance_test_demo.Square(side).perimeter() == expected_perimeter


def data_source():
    fruits = ["apple", "banana", "grapes"]
    for fruit in fruits:
        yield fruit


@pytest.mark.parametrize("d", data_source())
def test_my_test(d):
    print(d)


@mock.patch("functions.retrieve_fruit")
def test_retrieve_fruit_from_source(mock_variable):
    print("Running [mock]")
    mock_variable.return_value = "Mocked Apple"
    fruit = instance_test_demo.retrieve_fruit(1)

    assert fruit == "Mocked Apple"


@mock.patch("requests.get")
def test_get_users(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"id": 1, "name": "John Doe"}
    mock_get.return_value = mock_response
    data = instance_test_demo.get_users()
    assert data == {"id": 1, "name": "John Doe"}


@mock.patch("requests.get")
def test_get_users_error(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 400
    mock_get.return_value = mock_response
    with pytest.raises(requests.HTTPError):
        instance_test_demo.get_users()


# Fixture for a teacher
@pytest.fixture
def teacher():
    return instance_test_demo.Teacher("Professor Snape")


# Fixture for a list of students
@pytest.fixture
def students():
    return [Student("Harry Potter"), Student("Hermione Granger"), Student("Ron Weasley")]


# Fixture for a classroom with initial students
@pytest.fixture
def classroom(teacher, students):
    return Classroom(teacher, students, "Potions")


# Test to check if a student can be added to the classroom
def test_add_student(classroom):
    new_student = Student("Neville Longbottom")
    classroom.add_student(new_student)
    assert len(classroom.students) == 4


# Test to check if a student can be removed from the classroom
def test_remove_student(classroom):
    classroom.remove_student("Hermione Granger")
    assert len(classroom.students) == 2


# Test to check if a teacher can be changed
def test_change_teacher(classroom):
    new_teacher = Teacher("Professor McGonagall")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == "Professor McGonagall"


# Test to check if adding more than 10 students raises StudentsLimit exception
def test_students_limit_exception(classroom):
    with pytest.raises(instance_test_demo.StudentsLimit):
        for _ in range(10):
            classroom.add_student(instance_test_demo.Student("Random Student"))
