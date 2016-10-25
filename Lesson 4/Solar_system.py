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

sorted_solar_system = {}
def sorted_dict(dict_to_sort):
    for i in dict_to_sort.keys().sort:
        # sorted_solar_system.update(solar_system(i):solar_system.get(i))
        print solar_system.iteritems()


if __name__ == '__main__':
    for key, value in solar_system.iteritems():
        print "Планета {0} находится в {1} км от Солнца".format(key, value)
    # print solar_system.keys().sort
    sorted_dict(solar_system)
    print sorted_solar_system
    # for key, value in solar_system.iteritems():
    #     print "Планета {0} находится в {1} км от Солнца".format(key, value)
