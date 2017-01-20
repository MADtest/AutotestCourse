# -*- coding: utf-8 -*-

# I temp

# from Employee import Employee
#
# print Employee
# jim = Employee('Jim', 500)
# jim2 = Employee('Jim2', 500)
# jim3 = Employee('Jim3', 500)
# jim.display()
# print jim.get_count()
#
# print dir(jim)
# print jim.__dict__
# print jim.__doc__
# print Employee.__name__
# print jim.__module__
# print Employee.__bases__

#
# from Door import Door
# door1 = Door(1, 'open')
# door2 = Door(2, 'open')
# print door1.state
#
# print hex(id(Door.color))
# print hex(id(door1.color))
# print hex(id(door2.color))
#
# Door.color = 'Red'
#
# print Door.color
# print door1.color
# print hex(id(Door.color))
# print hex(id(door1.color))
# print hex(id(door2.color))
#
#
# print door1.__dict__
# print Door.__dict__
# print door2.__class__.__dict__['color']


class JustCounter(object):
    __secretCount = 0

    def count(self):
        self.__secretCount += 1
        print self.__secretCount


if __name__ == '__main__':
    counter1 = JustCounter()
    counter2 = JustCounter()

    print counter1._JustCounter__secretCount

    # print counter1.__secretCount

    print counter2._JustCounter__secretCount is counter1._JustCounter__secretCount

    counter1._JustCounter__secretCount
    print counter1._JustCounter__secretCount
    counter1._JustCounter__secretCount
    print counter1.__dict__
