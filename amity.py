from room import Room, LivingSpace, Office

from person import Fellow, Staff

import random


class Amity(object):
    """docstring for Amity"""

    def __init__(self):
        self.rooms = []
        self.livingspaces = []
        self.people = []
        self.fellows = []
        self.staff = []
        self.offices = []
        self.vacant_offices = []
        self.vacant_livingspaces = []

    def add_person(self, first_name, last_name, person_title,
                   wants_accomodation="N"):
        name = first_name + " " + last_name
        if person_title.upper() == "FELLOW":
            new_person = Fellow(name)
            new_id = str(new_person.person_id)
            self.people.append(new_person)
            self.fellows.append(new_person)
            self.allocate_office(new_person)
            if wants_accomodation.upper() == "Y":
                self.allocate_livingspace(new_person)
                self.add_person_successfully(
                    name, new_id, person_title, wants_accomodation)
            return
        elif person_title.upper() == "STAFF":
            new_person = Staff(name)
            new_id = str(new_person.person_id)
            self.people.append(new_person)
            self.staff.append(new_person)
            self.allocate_office(new_person)
            self.add_person_successfully(
                name, new_id, person_title, wants_accomodation)
            return
        else:
            print "Please enter 'Fellow' or 'Staff' as the job title"

    def allocate_office(self, new_person):
        """"Allocates offices"""
        if len(self.vacant_offices):
            self.workspace = random.choice(self.vacant_offices)
            self.workspace.occupants.append(new_person)
            print new_person.name + " assigned the office " + \
                self.workspace.room_name
            self.check_room_vacancy()
        else:
            print "No vacant offices at the moment,add one or try again later"

    def allocate_livingspace(self, new_person):
        """Allocates Living spaces"""
        if len(self.vacant_livingspaces):
            self.livespace = random.choice(self.vacant_livingspaces)
            self.livespace.occupants.append(new_person)
            print new_person.name + " assigned the livingspace " + \
                self.livespace.room_name
            self.check_room_vacancy()
        else:
            print "No vacant livingspaces at the moment, \
                add one or try again later"

    def check_room_vacancy(self):
        """Adds and removes rooms from vacancy lists \
        according to status of the room"""
        for office in self.offices:
            space = Office(office)
            if len(space.occupants) < space.max_occupancy:
                if office not in self.vacant_offices:
                    self.vacant_offices.append(office)
            elif len(office.occupants) >= office.max_occupancy:
                if office in self.vacant_offices:
                    self.vacant_offices.remove(office)
        for livingspace in self.livingspaces:
            space = Room(livingspace)
            if len(space.occupants) < space.max_occupancy:
                if livingspace not in self.vacant_livingspaces:
                    self.vacant_livingspaces.append(livingspace)
            elif len(space.occupants) >= space.max_occupancy:
                if livingspace in self.vacant_livingspaces:
                    self.vacant_livingspaces.remove(livingspace)

    def reallocate_person(self, person_id, new_room_name):
        pass

    def add_person_successfully(self, name, person_id,
                                person_title, wants_accomodation):
        print "You've successfully added \n" \
            + "\nName: " + name + " ID: " + person_id +\
            "\nJob title: " + person_title + \
            "\nWants accomodation: " + wants_accomodation

    def create_room(self, room_name, room_type):
        """Adds a new room in the system"""
        if room_name not in \
                [single_room.room_name for single_room in self.rooms]:
            if room_type.upper() == "OFFICE":
                new_room = Office(room_name)
                self.offices.append(new_room)
                self.rooms.append(new_room)
                self.vacant_offices.append(new_room)
                self.succesful_create_room(room_name, room_type)
            elif room_type.upper() == "LIVING":
                new_room = LivingSpace(room_name)
                self.livingspaces.append(new_room)
                self.vacant_livingspaces.append(new_room)
                self.rooms.append(new_room)
                self.succesful_create_room(room_name, room_type)
            else:
                print "Please enter 'Office' or 'Living' as the room type"
        else:
            print "Room already exists, try another name"

    def succesful_create_room(self, room_name, room_type):
        """Confirms creation of a new room"""
        print "Sucessfully created the following room \n"\
            "Room name: " + room_name + " "\
            "Room type: " + room_type + "\n"

    def load_people(self):
        pass

    def print_room(self, room_name):
        """Prints the occupants of a given room"""
        for room in range(len(self.rooms)):
            print room, " ", self.rooms[room].room_name
            if room_name == self.rooms[room].room_name:
                print room_name

                print "================================================"
                if len(self.rooms[room].occupants):
                    for member in range(len(self.rooms[room].occupants)):
                        print "{}.\t{}".format(
                            member + 1,
                            self.rooms[room].occupants[member])
                else:
                    print "Room has no occupants at the moment"
            else:
                print room_name + \
                    " not created yet, use 'create_room' to add it"

    def load_state(self):
        pass

    def save_state(self):
        pass

    def print_allocations(self, filename=None):
        pass

    def print_unallocated(self, filename=None):
        pass
