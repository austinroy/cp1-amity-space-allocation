class Room(object):
    """docstring for Room"""

    def __init__(self, room_name):
        self.room_name = room_name
        self.occupants = []
        self.max_occupancy = 0


class Office(Room):
    """docstring for Office"""

    def __init__(self, room_name):
        self.room_name = room_name
        self.max_occupancy = 6
        self.occupants = []
        self.room_type = "Office"


class LivingSpace(Room):
    """docstring for Office"""

    def __init__(self, room_name):
        self.room_name = room_name
        self.max_occupancy = 4
        self.occupants = []
        self.room_type = "Living"
