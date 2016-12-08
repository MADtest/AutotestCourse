# from Crop import Crop


class Animal(object):

    def __init__(self, name, growth_rate=2, food_need=5, water_need=3):
        self.name = name
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._growth = 0
        self._days_growing = 0
        self._type = 'generic'
        self._status = 'born'

    def needs(self):
        return {
            'food_need': self._food_need,
            'water_need': self._water_need}

    def report(self):
        return {
            'name': self.name,
            'type': self._type,
            'status': self._status,
            'growth': self._growth,
            'days_growing': self._days_growing}

    def _update_status(self):  # can't get how to save status
        if self._growth == 0:
            self._status = 'Born'
        elif 0 < self._growth <= 5:
            self._status = 'Baby'
        elif 5 < self._growth <= 10:
            self._status = 'Kid'
        elif 10 < self._growth <= 15:
            self._status = 'Mature'
        elif self._growth > 15:
            self._status = 'Old'

    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._growth += self._growth_rate
        self._days_growing += 1
        self._update_status()


class Cow(Animal):

    def __init__(self, name):
        super(Cow, self).__init__(name, 3, 4, 5)
        self._type = 'cow'


class Sheep(Animal):

    def __init__(self, name):
        super(Sheep, self).__init__(name, 5, 3, 4)
        self._type = 'sheep'


if __name__ == '__main__':
    cow = Animal('Nany', 3, 4, 5)
    print cow.report()



    # cow.auto_grow(10)
    # print cow.report()