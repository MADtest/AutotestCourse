# -*- coding: utf-8 -*-


class Door(object):

    color = 'brown'

    def __init__(self, number, state):
        self.number = number
        self.state = state

    def open(self):
        self.state = 'open'

    def close(self):
        self.close = 'close'

    @classmethod
    def knock(cls):
        print ('Knock! Knock!!!')


class SecurityDoor(Door):
    color = 'grey'
    locked = True

    def open(self):
        if not self.locked:
            print ('Opening')
            super(SecurityDoor, self).open()
            # Door.open(self)
            # self.state = 'open'


class CompositeDoor(object):
    color = 'composite'
    locked = True

    def __init__(self, number, state):
        self.door = Door(number, state)

    def open(self):
        if not self.locked:
            print ('Opening')
            self.door.open()

    def close(self):
        self.door.close()

    def __getattr__(self, attr):
        return getattr(self.door, attr)



if __name__ == '__main__':

    cdoor = CompositeDoor(1, 'open')
    print (cdoor.__dict__)
    print (cdoor.color)
    cdoor.open()
    cdoor.close()



    # sdoor = SecurityDoor(1, 'closed')
    # print (sdoor.open())
    # print (sdoor.color)
    # print (sdoor.locked)
    # print (sdoor.state)
    # print (sdoor.__class__.__dict__)
    # print (sdoor.__class__.__bases__[0].__dict__)


    # sdoor = SecurityDoor(1, 'closed')
    # print (sdoor.__dict__)
    # print (sdoor.color is Door.color)
    # print (sdoor.__class__.__dict__)
    # print (sdoor.__class__)
    # print (sdoor.__class__.__bases__)
    # print (sdoor.__class__.__bases__[0].__dict__)
    # print (sdoor.__class__.__bases__[0].__dict__['color'])
    # print (sdoor.__class__.__bases__[0].__dict__['knock'])
    # print (sdoor.__class__.__bases__[0].__dict__['knock'].__get__(sdoor, Door))()



    # door1 = Door(1, 'open')
    # print (door1.__dict__)
    # door2 = Door(2, 'closed')
    # print (door1.knock)
    # print (door2.knock)
    # print (Door.knock)
    # print (door1.open)
    # print (type(Door.open))
    # print (door1.__class__.__dict__['knock'])
    # print (type(door1.__class__.__dict__['knock']))
    # print (type(door1.__class__.__dict__['open']))
    # print (door1.__class__.__dict__['knock'].__get__(door1, Door))
    # print (type(door1.__class__.__dict__['knock'].__get__(door1, Door)))
