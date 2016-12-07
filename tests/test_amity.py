import unittest

from amity import Amity

from room import Room, Office, LivingSpace

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
        # self.livingspace1 = self.amity.livingspace[0]

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
        livingspace = LivingSpace(self)
        self.assertEqual(4, livingspace.max_occupancy)
        """Ensure livingspace has a capacity of 4"""

    def test_print_room(self):
        """Tests for the print_room function"""
        room = Room(self)
        self.assertEqual([], room.occupants)
        pass

    def test_add_person(self):
        """Test addition of people"""
        #  Check if people added in setup
        self.assertEqual(2, len(self.amity.people))
        self.assertEqual(1, len(self.amity.fellows))
        self.assertEqual(1, len(self.amity.staff))

    # def test_person_is_fellow_or_staff(self):
    #     """Validates that the person added has a title of either fellow or staff
    #      and nothing other than those two"""
    #     self.assertTrue((
    #                     self.person.person_title == "Fellow" or
    #                     self.person.person_title == "Staff"),
    #                     msg="person_title should be either Fellow or Staff")
    def test_automatic_allocation_new_person(self):
        """Test new people are automoatically assigned offices"""
        # Ensure that these people have been appended to rooms' occupants
        self.assertEqual(2, len(self.office1.occupants),
                         msg="Newly added people should \
be added to room occupants")

    def test_rellocate_person(self):
        """Tests the rellocation of people"""
        # Add a new office and assign it to a variable
        # self.amity.create_room(
        #     "Office2",
        #     "Office"
        # )
        # self.office2 = self.amity.offices[1]
        # self.randomstaff = self.amity.staff[0]

        # """Test the reallocation of Random Staff to office 2 from office 1"""
        # self.amity.reallocate_person({
        #     int(self.randomstaff.person_id),
        #     "Office2",
        # })
        # # office2 = self.amity.offices[1]
        # # Test that Random Staff now occupies Office2
        # self.assertEqual(1, len(self.office2.occupants))
        # self.assertEqual("Random Staff", self.office2.occupants[0],
        #                  msg="Occupant not added to list of occupants")

        # # Test that Random Staff no longer in Office1 occupants
        # self.assertEqual(0, len(self.office1.occupants))
        pass


if __name__ == '__main__':
    unittest.main()
