# -*- coding: utf-8 -*-
solar_system = {
    'Mercury': 57910000,
    'Venus': 108200000,
    'Earth': 149600000,
    'Mars': 227940000,
    'Jupiter': 778330000,
    'Saturn': 1424600000,
    'Uranus': 2873550000,
    'Neptune': 4501000000,
    'Pluto': 5945900000}

main_star = 'Sun'
main_unit = 'km'


def fill_planet_data_to_template():
    with open('C:\MS\System.txt') as file:
        template = file.readline()
    with open('C:\MS\Result_system.txt', 'a') as result_file:
        for i in range(len(solar_system)):
            result_file.write(template.format(
                planet=solar_system.keys()[i], distance=solar_system.values()[i], unit=main_unit, star=main_star))

if __name__ == '__main__':
    fill_planet_data_to_template()
