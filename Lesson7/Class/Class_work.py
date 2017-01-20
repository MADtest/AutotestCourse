# -*- coding: utf-8 -*-
#
#
#
# ﻿Задания на ООП:
#
# 1. Создать классы: Point, Shape, Rectangular, Square, Triangular, Circle.
#    Все классы наследуются от Shape, кроме Point. В классе Shape есть метод draw(), get_area(), get_perimeter, to_string().
#    У Rectangular, Square, Triangular, Circle есть переопределенные методы get_perimeter, get_area(), to_string(), соотвествующие конструкторы.
#    Классы также должны переопределять метод draw.
#
#    - Создать класс Rectangular. У него есть длина, ширина, конструктор. Также есть методы get_area(), get_perimeter.
#    - Создать класс Circle. У него есть радиус, конструктор. Также есть методы get_area(), get_perimeter.
#    - Создать класс Point. У него есть x, y. Также есть метод get_distance_to(Point).
#    - Создать класс Triangle. У него есть три точки. Также есть методы get_area(), get_perimeter.
#    - Создать класс Square. У него есть сторона. Также есть методы get_area(), get_perimeter.
#    - Добавить в конструктор Rectangular, Square, Сircle точку, добавить метод get_location - возвращает центр фигуры.
#    - Создать класс Shape с методами draw(), get_area(), get_perimeter, to_string() и унаследовать все фигуры от него.
#       Переопределить соотвествющие методы.
#    - Для метода draw использовать модуль turtle (https://opentechschool.github.io/python-beginners/ru)
#
# __str__ для позврата строки типа '{зашейплено} от {фигуры} с {параметрами} == I'm in shape of {} with {}'

import math


class Shape(object):

    def draw(self):
        pass

    def get_area(self):
        return 0

    def perimeter(self):
        return 0

    # def __str__(self):
    #     return 'I am shape'

    def __cmp__(self, figure2):
        if self.get_area() == figure2.get_area():
            return 0
        if self.get_area() > figure2.get_area():
            return 1
        if self.get_area() < figure2.get_area():
            return -1

    @staticmethod
    def get_max_shape(list_of_figures):
        largiest_figure = list_of_figures[0]
        for figure in list_of_figures[1:]:
            if figure.get_area() > largiest_figure.get_area():
                largiest_figure = figure
        return largiest_figure




class Rectangular(Shape):

    def __init__(self, lenth, width):
        self.lenth = lenth
        self.width = width

    def get_area(self):
        return self.lenth*self.width

    def get_perimeter(self):
        return 2 * (self.lenth+self.width)


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi*(self.radius**2)

    def get_perimeter(self):
        return 2 * math.pi * self.radius


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_distance_to(self, Point):
        return math.sqrt((Point.x - self.x) ** 2 + (Point.y - self.y) ** 2)


class Triangle(Shape):

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @property
    def a(self):
        return self.x.get_distance_to(self.y)

    @property
    def b(self):
        return self.x.get_distance_to(self.y)

    @property
    def c(self):
        return self.x.get_distance_to(self.y)

        # self.a = self.x.get_distance_to(self.y)
        # self.b = self.y.get_distance_to(self.z)
        # self.c = self.z.get_distance_to(self.x)

    def get_area(self):
        p = (self.a + self.b + self.c)/2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def get_perimeter(self):
        return self.a + self.b + self.c


class Square(Shape):

    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side


if __name__ == '__main__':
    # print Rectangular(3, 4).get_area()
    # print Rectangular(3, 4).get_perimeter()
    #
    # print Circle(5).get_area()
    # print Circle(5).get_perimeter()
    #
    # print Square(5).get_area()
    # print Square(5).get_perimeter()
    #
    # print Point(4, 5).get_distance_to(Point(5, 6))
    #
    # print Triangle(Point(0, 0), Point(0, 3), Point(3, 3)).get_area()
    # print Triangle(Point(0, 0), Point(0, 3), Point(3, 3)).get_perimeter()
    # print Triangle(Point(1, 1), Point(-2, 4), Point(-2, -2)).get_area()
    # print Triangle(Point(1, 1), Point(-2, 4), Point(-2, -2)).get_perimeter()

    p1 = Point(1, 1)
    p2 = Point(-2, 4)
    p3 = Point(-2, -2)

    tr = Triangle(p1, p2, p3)

    # tr.a = 99

    print tr.get_area()
    cr = Circle(5)
    print cr.get_area()

    # print tr.__cmp__(cr)

    sc = Square(4)
    print sc.get_area()
    rc = Rectangular(4, 4)
    print rc.get_area()

    # print sc.__cmp__(rc)

    print Shape.get_max_shape([tr, cr, sc, rc])

    print tr == cr
    print sc == rc
