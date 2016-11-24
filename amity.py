from room import Room, LivingSpace, Office

from person import Person, Fellow, Staff


class Amity(object):
    """docstring for Amity"""
    rooms = []
    offices = []
    livingspaces = []
    people = []
    fellows = []
    staff = []

    def __init__(self):
        rooms = []
        offices = []
        livingspaces = []

    def add_person(self, first_name, last_name, person_title,
                   wants_accomodation="N"):
        if person_title == "Fellow":
            person = Fellow()
        elif person_title == "Staff":
            person = Staff()
        else:
            print "Please enter 'Fellow' or 'Staff' as the job title"

    def reallocate_person(self, person_id, room_name):
        pass

    def create_room(self, room_name, room_type):
        if room_type == "Office":
            pass
        elif room_type == "Living":
            pass
        else:
            print "Please enter 'Fellow' or 'Staff' as the job title"

    def load_people(self):
        pass

    def print_room(self):
        pass

    def load_state(self):
        pass

    def save_state(self):
        pass

    def print_allocations(self, filename=None):
        pass

    def print_unallocated(self, filename=None):
        pass
