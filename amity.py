from room import Room, LivingSpace, Office

from person import Fellow, Staff

import random

import sqlite3


class Amity(object):
    """docstring for Amity"""

    def __init__(self, dbname="amity.db"):
        self.rooms = []
        self.livingspaces = []
        self.people = []
        self.fellows = []
        self.staff = []
        self.offices = []
        self.vacant_offices = []
        self.vacant_livingspaces = []
        self.vacant_rooms = []
        self.unallocated = []
        self.conn = sqlite3.connect(dbname)
        self.connect = self.conn.cursor()

    def add_person(self, first_name, last_name, person_title,
                   wants_accomodation="N"):
        name = first_name + " " + last_name
        allocated = False
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
            if not allocated:
                self.unallocated.append(new_person)
            return
        elif person_title.upper() == "STAFF":
            new_person = Staff(name)
            new_id = str(new_person.person_id)
            self.people.append(new_person)
            self.staff.append(new_person)
            self.allocate_office(new_person)
            self.add_person_successfully(
                name, new_id, person_title, wants_accomodation)
            if not allocated:
                self.unallocated.append(new_person)
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
            allocated = True
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
            allocated = True
            self.check_room_vacancy()
        else:
            print "No vacant livingspaces at the moment," \
                "add one or try again later"

    def check_room_vacancy(self):
        """Adds and removes rooms from vacancy lists \
        according to status of the room"""
        for office in self.offices:
            space = Office(office)
            if len(space.occupants) < space.max_occupancy:
                if office not in self.vacant_offices:
                    self.vacant_offices.append(office)
                    self.vacant_rooms.append(office)
            elif len(office.occupants) >= office.max_occupancy:
                if office in self.vacant_offices:
                    self.vacant_offices.remove(office)
                    self.vacant_rooms.remove(office)
        for livingspace in self.livingspaces:
            space = Room(livingspace)
            if len(space.occupants) < space.max_occupancy:
                if livingspace not in self.vacant_livingspaces:
                    self.vacant_livingspaces.append(livingspace)
                    self.vacant_rooms.append(livingspace)
            elif len(space.occupants) >= space.max_occupancy:
                if livingspace in self.vacant_livingspaces:
                    self.vacant_livingspaces.remove(livingspace)
                    self.vacant_rooms.remove(livingspace)

    def reallocate_person(self, person_id, new_room_name):
        """Reallocates people to new rooms"""
        moving_person = None

        for peep in self.people:
            if peep.person_id == person_id:
                moving_person = peep

        if moving_person is None:
            print "That person ID does not exist, try another"
            return

        for room in self.rooms:
            if room.room_name == new_room_name:
                new_room = room

        if new_room_name not in [room.room_name for room in self.vacant_rooms]:
            print "The room enterred doesn't exist or is full, enter another"
            return

        if moving_person.person_title == "Staff":
            """Prevent staff from being allocated living spaces"""
            if new_room.room_type == "Living":
                print "Staff members cannot be allocated " \
                    "living spaces."
                return

        for room in self.vacant_rooms:
            if moving_person.person_id in \
                    [human.person_id for human in room.occupants]:
                if new_room == room:
                    """Prevent person from being allocated the same room"""
                    print moving_person.name + " is already an occupant" \
                        " of the room " + new_room.name + "."
                    return
                else:
                    """Remove person from current office"""
                    room.occupants.remove(moving_person)
        """Add person to new room"""
        new_room.occupants.append(moving_person)
        print "You have successfully allocated " + moving_person.name + \
            " of Employee ID " + str(moving_person.person_id) + \
            "\nthe following room: " + new_room.room_name

    def add_person_successfully(self, name, person_id,
                                person_title, wants_accomodation):
        print "You've successfully added \n" \
            + "\nName: " + name + " ID: " + person_id +\
            "\nJob title: " + person_title + \
            "\nWants accomodation: " + wants_accomodation

    def create_room(self, room_name, room_type):
        """Adds a new room in the system"""
        if room_name in \
                [single_room.room_name for single_room in self.rooms]:
            print "Room already exists, try another name"
            return
        if room_type.upper() == "OFFICE":
            new_room = Office(room_name)
            self.offices.append(new_room)
            self.rooms.append(new_room)
            self.vacant_offices.append(new_room)
            self.vacant_rooms.append(new_room)
            self.succesful_create_room(room_name, room_type)
        elif room_type.upper() == "LIVING":
            new_room = LivingSpace(room_name)
            self.livingspaces.append(new_room)
            self.rooms.append(new_room)
            self.vacant_livingspaces.append(new_room)
            self.vacant_rooms.append(new_room)
            self.succesful_create_room(room_name, room_type)
        else:
            print "Please enter 'Office' or 'Living' as the room type"

    def succesful_create_room(self, room_name, room_type):
        """Confirms creation of a new room"""
        print "Sucessfully created the following room \n"\
            "Room name: " + room_name + " "\
            "Room type: " + room_type + "\n"

    def load_people(self, arg):
        filename = arg["<filename>"]
        with open(filename, 'r') as people_file:
            people = people_file.readlines()
            for guy in people:
                guy = guy.split()
                first_name = guy[0]
                last_name = guy[1]
                person_title = guy[2]
                if len(guy) == 4:
                    wants_accomodation = guy[3]
                else:
                    wants_accomodation = "N"
                self.add_person(first_name, last_name, person_title,
                                wants_accomodation)

    def print_room(self, room_name):
        """Prints the occupants of a given room"""
        for room in self.rooms:
            if room_name == self.rooms[room].room_name:
                print room_name

                print "=" * 75
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
        """Loads data from a db"""
        pass

    def create_tables(self):
        '''Creates the database tables'''
        try:
            self.connect.execute(
                """CREATE TABLE IF NOT EXISTS People\
                (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                Name TEXT, Person_Title TEXT, Person_id TEXT)""")

            self.connect.execute(
                """CREATE TABLE IF NOT EXISTS Rooms
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 Room_Name TEXT, Room_Type TEXT, Members TEXT)""")
        except sqlite3.IntegrityError:
            return False

    def save_state(self, arg):
        """Saves the state of the data"""
        self.create_tables()
        for person in self.people:
            self.connect.execute(
                "INSERT INTO People(Name, Person_Title, Person_id ) VALUES(?, ?, ?)",
                [str(person.name), str(person.person_title),
                 str(person.person_id)])
            self.conn.commit()

        for room in self.rooms:
            self.connect.execute(
                "INSERT INTO Rooms(Room_Name, Room_type, Members) VALUES(?, ?, ?)",
                [str(room.room_name), str(room.room_type),
                 str([ocu.name for ocu in room.occupants])])
            self.conn.commit()

    def print_allocations(self, arg):
        details = "ALLOCATIONS\n" + "=" * 75 + "\n"
        if not self.rooms:
            details = "There are no rooms in the system at the moment"
        for room_to_print in self.rooms:
            details += room_to_print.room_name + "\n"
            details += "=" * 75 + "\n"
            if room_to_print.occupants:
                details += "\n".join(human.name for human in
                                     room_to_print.occupants) + "\n \n"
            else:
                details += "Room has no occupants at the moment" + "\n \n"
        print details
        if arg["--o"]:
            with open(arg["--o"], 'wt') as file:
                file.write(details)
                print "Allocations were saved to: {}".format(arg["--o"])

    def print_unallocated(self, arg):
        details = "UNALLOCATED PEOPLE\n" + "=" * 75 + "\n"
        if not self.unallocated:
            details += "There are no unallocated people at the moment"
        for person in self.unallocated:
            details += "{} {}\n".format(person.name, person.person_id)

        print details
        if arg["--o"]:
            with open(arg["--o"], 'wt') as file:
                file.write(details)
                print "Unallocated saved to: {}".format(arg["--o"])
