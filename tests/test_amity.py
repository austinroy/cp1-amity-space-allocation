import unittest

import os

from amity import Amity

from room import Room, Office, LivingSpace
import sqlite3

from person import Person


class TestAmity(unittest.TestCase):
    """Unit tests to test functions in the Person Class"""

    def setUp(self):
        self.amity = Amity()

        """Create sample living space"""
        self.amity.create_room(
            "LivingSpace1",
            "Living"
        )

        """Create sample office"""
        self.amity.create_room(
            "Office1",
            "Office"
        )
        self.office1 = self.amity.offices[0]
        self.livingspace1 = self.amity.livingspaces[0]

        """Add fellow that wants accomodation"""
        self.amity.add_person(
            "Random",
            "Fellow",
            "Fellow",
            "Y"
        )

        """Add staff member that wants accomodation"""
        self.amity.add_person(
            "Random",
            "Staff",
            "Staff",
            "Y"
        )

    def test_create_room(self):
        """Test creation of rooms"""
        # Check rooms created added to relevant lists
        self.assertEqual(2, len(self.amity.rooms))
        self.assertEqual(1, len(self.amity.livingspaces))
        self.assertEqual(1, len(self.amity.offices))

        """Validates that duplicate rooms are not added"""
        self.amity.create_room(
            "Office1",
            "Office"
        )
        # Duplicate rooms not added to any list
        self.assertEqual(2, len(self.amity.rooms))
        self.assertEqual(1, len(self.amity.offices))

    def test_office_has_capacity_of_6(self):
        """Ensure office has a capacity of 6"""
        office = Office(self)
        self.assertEqual(6, office.max_occupancy)

    def test_livingspace_has_capacity_of_4(self):
        """Ensure livingspace has a capacity of 4"""
        livingspace = LivingSpace(self)
        self.assertEqual(4, livingspace.max_occupancy)

    def test_print_room(self):
        """Tests for the print_room function"""
        room = Room(self)
        self.assertEqual([], room.occupants)

    def test_add_person(self):
        """Test addition of people"""
        #  Check if people added in setup
        self.assertEqual(2, len(self.amity.people))
        self.assertEqual(1, len(self.amity.fellows))
        self.assertEqual(1, len(self.amity.staff))

    def test_automatic_allocation_new_person(self):
        """Test new people are automoatically assigned offices"""
        # Ensure that these people have been appended to rooms' occupants
        self.assertEqual(2, len(self.office1.occupants),
                         msg="Newly added people should "
                         "be added to room occupants")

    def test_rellocate_person(self):
        """Tests the rellocation of people"""
        # Add a new office and assign it to a variable
        self.amity.create_room(
            "Office2",
            "Office"
        )
        self.office2 = self.amity.offices[1]
        self.randomstaff = self.amity.staff[0]

        """Test the reallocation of Random Staff to office 2 from office 1"""
        self.amity.reallocate_person(
            int(self.randomstaff.person_id),
            "Office2",
        )
        # office2 = self.amity.offices[1]
        # Test that Random Staff now occupies Office2
        self.assertEqual(1, len(self.office2.occupants))
        self.assertEqual("Random Staff", self.office2.occupants[0].name,
                         msg="Occupant not added to list of occupants")

        # Test that Random Staff no longer in Office1 occupants
        self.assertEqual(1, len(self.office1.occupants))

    def test_print_allocations(self):
        """
        Test that allocations are displayed on the screen
        and printed to a text file if specified
        """
        self.amity.print_allocations({
            "--o": "allocations.txt"
        })
        # Confirm that file is created
        self.assertTrue(os.path.exists("allocations.txt"))
        # Confirm data is in file
        with open("allocations.txt") as allocations:
            lines = allocations.readlines()
            self.assertTrue("LivingSpace1\n" in lines)
            self.assertTrue("Office1\n" in lines)
            self.assertTrue("Random Fellow\n" in lines)
        os.remove("allocations.txt")

    def test_print_unallocated(self):
        """Test that unallocated people are displayed on the screen
        and printed to a text file if specified"""
        self.amity.print_unallocated({
            "--o": "unallocated.txt"
        })
        # Confirm that file is created
        self.assertTrue(os.path.exists("unallocated.txt"))
        # Confirm data is in file
        with open("unallocated.txt") as unallocated:
            lines = unallocated.readlines()
            self.assertTrue("LivingSpace1\n" in lines)
            self.assertTrue("Office1\n" in lines)
            self.assertTrue("Random Fellow\n" in lines)
        os.remove("unallocated.txt")

    def test_check_office_vacancy(self):
        """Test that vacant offices are added to relevant list"""
        # Add a new office
        self.amity.create_room("RandomOffice", "Office")

        self.amity.check_room_vacancy()

        # Check if the new office has been appended to relevant lists
        self.assertEqual(2, len(self.amity.vacant_offices))

    def test_check_livingspace_vacancy(self):
        """Test that vacant living spaces are added to relevant list"""
        # Add a new office
        self.amity.create_room("RandomLiving", "Living")

        self.amity.check_room_vacancy()

        # Check if the new office has been appended to relevant lists
        self.assertEqual(2, len(self.amity.vacant_livingspaces))

    def test_load_people(self):
        """Tests that people are loaded from an external text file"""

        """Add office to have more vacant offices for people from text file """
        self.amity.create_room(
            "OfficeC",
            "Office"
        )

        self.amity.load_people({"<filename>": "people.txt"})
        # People from file are added to application
        self.assertEqual(9, len(self.amity.people))
        self.assertEqual(5, len(self.amity.fellows))
        self.assertEqual(4, len(self.amity.staff))

    def test_save_state(self):
        """Tests that the current state of the application is saved to a DB"""
        conn = sqlite3.connect('amity.db')
        cursor = conn.cursor()
        self.assertFalse(self.amity.create_tables("amity.db"), False)
        self.amity.save_state({"--db":"amity.db"})

        cursor.execute("SELECT * from People")
        for row in cursor:
            # import ipdb; ipdb.set_trace()
            self.assertEqual(row[0], 1)
            self.assertEqual(row[1], 'Random Fellow')
            self.assertEqual(row[2], 'Fellow')
            break

    def test_load_state(self):
        """Tests the loading of data from an database"""
        pass

    def tearDown(self):
        self.amity = None


if __name__ == '__main__':
    unittest.main()
