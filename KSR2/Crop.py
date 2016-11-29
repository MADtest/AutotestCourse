# -*- coding: utf-8 -*-
import random


class Crop(object):
    __growth = 0
    __days_growing = 0
    __type = 'generic'
    __status = 'seed'

    def __init__(self, growth_rate=2, light_need=5, water_need=3):
        self.__growth_rate = growth_rate
        self.__light_need = light_need
        self.__water_need = water_need

    @property
    def growth(self):
        return self.__growth

    @property
    def days_growing(self):
        return self.__days_growing

    @property
    def type(self):
        return self.__type

    @property
    def status(self):
        return self.__status

    @property
    def growth_rate(self):
        return self.__growth_rate

    @property
    def light_need(self):
        return self.__light_need

    @property
    def water_need(self):
        return self.__water_need

    def needs(self):
        return {'light_need': self.light_need, 'water_need': self.water_need}

    def report(self):
        return {'type': self.type, 'status': self.status, 'growth': self.growth, 'days_growing': self.days_growing}

    def __update_status(self):  # can't get how to save status
        if self.growth == 0:
            self.__status = 'Seed'
        elif 0 < self.growth <= 5:
            self.__status = 'Seeding'
        elif 5 < self.growth <= 10:
            self.__status = 'Young'
        elif 10 < self.growth <= 15:
            self.__status = 'Mature'
        elif self.growth > 15:
            self.__status = 'Old'

    def grow(self, current_available_light, current_available_water):
        if current_available_light >= self.light_need and current_available_water >= self.water_need:
            self.__growth += self.__growth_rate
        self.__days_growing += 1
        self.__update_status()

    def auto_grow(self, number_of_days=5):
        for i in range(number_of_days):
            self.grow(random.randint(1, 10), random.randint(1, 10))

    def manual_grow(self):
        print 'Input available light (1 to 10)'
        available_light = input()
        while available_light not in range(1, 10):
            print 'Value should be from 1 to 10'
            available_light = input()
        print 'Input available water (1 to 10)'
        available_water = input()
        while available_water not in range(1, 10):
            print 'Value should be from 1 to 10'
            available_water = input()
        self.grow(available_light, available_water)

__e = 0


def display_menu():
    test_crop = Crop()
    print 'Hello, this a crop growing emulator, choose an action'
    while __e != 1:
        print ' 1 for manually growing the crop '
        print ' 2 for automatically growing the crop '
        print ' 3 to get the crop report '
        print ' 4 to exit'
        get_menu_choice()


def get_menu_choice():
    choice = input()
    if choice in (1, 2, 3):
        manage_crop(choice)
    elif choice == 4:
        print 'Good buy'
        __e = 1
    else:
        print 'Incorrect input'
        display_menu()


def manage_crop(choice):
    if choice == 1:
        test_crop.manual_grow()
    elif choice == 2:
        test_crop.auto_grow()
    elif choice == 3:
        test_crop.report()

if __name__ == '__main__':
    crop1 = Crop(2, 4, 3)
    crop2 = Crop(3, 5, 4)
    print crop1.growth, crop1.days_growing, crop1.growth_rate, crop1.light_need, crop1.water_need, crop1.type,\
        crop1.status
    print crop2.growth, crop2.days_growing, crop2.growth_rate, crop2.light_need, crop2.water_need, crop2.type,\
        crop2.status
    print crop1.needs()
    print crop2.report()

    print crop1.report()
    crop1.auto_grow()
    print crop1.report()
    # uncommit to check manual_grow()
    # crop1.manual_grow()
    # print crop1.report()

    display_menu()

