# -*- coding: utf-8 -*-
# The class for employes

class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def get_count(self):
        return Employee.emp_count

    def display(self):
        print ('I am employee. My name is ' + self.name)

