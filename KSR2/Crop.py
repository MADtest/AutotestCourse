# -*- coding: utf-8 -*-
import random
from Animals import Cow, Sheep

class Crop(object):

    def __init__(self, growth_rate=2, light_need=5, water_need=3):
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._growth = 0
        self._days_growing = 0
        self._type = 'generic'
        self._status = 'seed'

    @property
    def growth(self):
        return self._growth

    @property
    def days_growing(self):
        return self._days_growing

    @property
    def type(self):
        return self._type

    @property
    def status(self):
        return self._status

    @property
    def growth_rate(self):
        return self._growth_rate

    @property
    def light_need(self):
        return self._light_need

    @property
    def water_need(self):
        return self._water_need

    def needs(self):
        return {
            'light_need': self._light_need,
            'water_need': self._water_need}

    def report(self):
        return {
            'type': self._type,
            'status': self._status,
            'growth': self._growth,
            'days_growing': self._days_growing}

    def _update_status(self):  # can't get how to save status
        if self._growth == 0:
            self._status = 'Seed'
        elif 0 < self._growth <= 5:
            self._status = 'Seedling'
        elif 5 < self._growth <= 10:
            self._status = 'Young'
        elif 10 < self._growth <= 15:
            self._status = 'Mature'
        elif self._growth > 15:
            self._status = 'Old'

    def grow(self, current_available_light, current_available_water):
        if current_available_light >= self._light_need and current_available_water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()

    def auto_grow(self, number_of_days=5):
        for i in range(number_of_days):
            self.grow(random.randint(1, 10), random.randint(1, 10))

    def manual_grow(self):
        print 'Input available light (1 to 10)'  # use 'try' structure
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


def display_menu(test_crop):
    # test_crop = Crop()

    print 'Choose an action:'
    while True:
        print ' 1 for manually growing the crop '
        print ' 2 for automatically growing the crop '
        print ' 3 to get the crop report '
        print ' 4 to exit'
        get_menu_choice(test_crop)


def get_menu_choice(test_crop):
    choice = input()
    if choice in (1, 2, 3):
        manage_crop(choice, test_crop)
    elif choice == 4:
        print 'Good buy'
        exit()
    else:
        print 'Incorrect input'
        display_menu(test_crop)


def manage_crop(choice, test_crop):
    if choice == 1:
        test_crop.manual_grow()
    elif choice == 2:
        test_crop.auto_grow()
    elif choice == 3:
        print test_crop.report()


def initiate_crop():
    is_valid = False
    while is_valid is not True:
        print ('Please choose crop or animal type:\n'
               ' 1 for wheat\n'
               ' 2 for potato\n'
               ' 3 for cow\n'
               ' 4 for sheep\n')
        input_value = raw_input('Option selected:')
        if input_value.isdigit() and int(input_value) in (1, 2, 3, 4):
            is_valid = True
        else:
            print('{} is not a valid option. Please choose from 1 to 2'.format(input_value))
    if int(input_value) == 1:
        return Wheat(3, 4, 4)
    elif int(input_value) == 2:
        return Potato(4, 3, 3)
    elif int(input_value) == 3:
        return Cow('Cocow')
    elif int(input_value) == 4:
        return Sheep('Shippy')


class Wheat(Crop):

    def __init__(self, growth_rate=2, light_need=5, water_need=3):
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._growth = 0
        self._days_growing = 0
        self._type = 'wheat'
        self._status = 'seed'

    # def grow(self, current_available_light, current_available_water):
    #     if current_available_light >= self._light_need and current_available_water >= self._water_need:
    #         if self.status == 'Seedling':
    #             mult = 1.5
    #         elif self.status == 'Young':
    #             mult = 1.25
    #         elif self.status == 'Old':
    #             mult = 0.5
    #         else:
    #             mult = 1
    #         self._growth_rate *= mult
    #         self._growth += self._growth_rate
    #     self._days_growing += 1
    #     self._update_status()
    #
    def _update_status(self):
        status = self.status
        super(Wheat, self)._update_status()
        if status is not self.status:
            if self.status == 'Seedling':
                self._growth_rate *= 1.5
            elif self.status == 'Young':
                self._growth_rate *= 1.25
            elif self.status == 'Old':
                self._growth_rate *= 0.5
        print self._growth_rate


class Potato(Crop):

    def __init__(self, growth_rate=2, light_need=5, water_need=3):
        self._growth_rate = growth_rate
        self._light_need = light_need
        self._water_need = water_need
        self._growth = 0
        self._days_growing = 0
        self._type = 'potato'
        self._status = 'seed'

    def _update_status(self):
        status = self.status
        super(Potato, self)._update_status()
        if status is not self.status:
            if self.status == 'Seedling':
                self._growth_rate *= 1.5
            elif self.status == 'Young':
                self._growth_rate *= 1.25
        # print self._growth_rate



if __name__ == '__main__':
    crop1 = Crop(3, 5, 4)
    crop2 = Crop(2, 4, 5)
    print crop1._growth, crop1._days_growing, crop1._growth_rate, crop1._light_need, crop1._water_need, crop1._type,\
        crop1._status
    print crop2._growth, crop2._days_growing, crop2._growth_rate, crop2._light_need, crop2._water_need, crop2._type,\
        crop2._status
    print crop1.needs()
    print crop2.report()

    print crop1.report()
    crop1.auto_grow()
    print crop1.report()
    # uncommit to check manual_grow()
    # crop1.manual_grow()
    # print crop1.report()

    # display_menu()
    cropw = Wheat(2, 4, 4)
    # print cropw.report()
    # cropw.manual_grow()
    # cropw.auto_grow(10)
    # print cropw._growth_rate
    # print cropw.report()
    cropp = Potato(2, 4, 4)
    print cropw.report()
    # cropw.manual_grow()
    cropp.auto_grow(10)
    # print cropw._growth_rate
    print cropp.report()

    my_crop = initiate_crop()
    display_menu(my_crop)
