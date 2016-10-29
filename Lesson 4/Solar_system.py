# -*- coding: utf-8 -*-
import collections, operator, random
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


def system(system_dict):
    for key, value in system_dict.iteritems():
        print "Планета {0} находится в {1} км от Солнца".format(key, value)


def sort_by_planet(system_dict):
    sorted_solar_system = collections.OrderedDict(sorted(system_dict.items()))
    print "Sorted by planet name:"
    for key, value in sorted_solar_system.iteritems():
        print "Планета {0} находится в {1} км от Солнца".format(key, value)


def sort_by_distance(system_dict):
    sorted_by_distance = sorted(system_dict.items(), key=operator.itemgetter(1))
    print "Sorted by distance:"
    for x, y in sorted_by_distance:
        print "Планета {0} находится в {1} км от Солнца".format(x, y)

def random_planet_info(system_dict):
    print "Random planet's info:"
    key = random.choice(system_dict.keys())
    print "Планета {0} находится в {1} км от Солнца".format(key, system_dict.get(key))


if __name__ == '__main__':
    system(solar_system)
    sort_by_planet(solar_system)
    sort_by_distance(solar_system)
    random_planet_info(solar_system)