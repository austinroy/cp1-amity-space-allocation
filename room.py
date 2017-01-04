class Room(object):
    """
    Main room class that holds attributes common to all room types
    """

    def __init__(self, room_name):
        self.room_name = room_name
        self.occupants = []


class Office(Room):
    """
    Class that contains attributes specific to the office room type
    """
    max_occupancy = 6
    room_type = "Office"

    def __init__(self, room_name):
        super(Office, self).__init__(room_name)

    def isvacant(self):
        return len(self.occupants) < self.max_occupancy


class LivingSpace(Room):
    """
    Class that contains attributes specific to the office room type
    """
    max_occupancy = 4
    room_type = "Living"

    def __init__(self, room_name):
        super(LivingSpace, self).__init__(room_name)

    def isvacant(self):
        return len(self.occupants) < self.max_occupancy
