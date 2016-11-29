# -*- coding: utf-8 -*-

import Crop


class ManagementMenu(object):

    def display_menu(self):
        print 'Hello, this a crop growing emulator, choose an action'
        print ' 1 for manually growing the crop '
        print ' 2 for automatically growing the crop '
        print ' 3 to get the crop report '
        print ' 0 to exit'
        self.get_menu_choice()

    def get_menu_choice(self):
        choice = input()
        if choice in (0, 1, 2, 3):
            if choice == 0:
                print 'Good buy'
            elif choice == 1:
                Crop.manual_grow
            elif choice == 2:
                Crop.auto_grow
            elif choice == 3:
                Crop.report

        else:
            print 'Incorrect input'
            self.display_menu()

    def manage_crop(self):
        pass

if __name__ == '__main__':
    pass