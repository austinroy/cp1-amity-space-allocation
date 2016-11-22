import unittest

from amity import Amity

from room import Office, LivingSpace


class TestAmity(unittest.TestCase):
    """Unit tests to test functions in the Person Class"""

    def setUp(self):
        self.amity = Amity()

        """Create sample living space"""
        self.amity.create_room({
            "<room_name>": ["LivingSpace1"],
            "Living": True,
            "Office": False
        })

        """Create sample office"""
        self.amity.create_room({
            "<room_name>": ["Office1"],
            "Living": False,
            "Office": True
        })
        self.office1 = self.amity.offices[0]
        self.livingspace1 = self.amity.livingspace[0]

        """Add fellow that wants accomodation"""
        self.person.add_person({
            "<first_name>": "Random",
            "<last_name>": "Fellow",
            "<wants_accomodation>": "Y",
            "Fellow": True,
            "Staff": False
        })

        """Add staff member that wants accomodation"""
        self.person.add_person({
            "<first_name>": "Random",
            "<last_name>": "Staff",
            "<wants_accomodation>": "Y",
            "Fellow": False,
            "Staff": True
        })

    def test_create_room(self):
        """Test creation of rooms"""
        # Check rooms created added to relevant lists
        self.assertEqual(2, len(self.room.rooms))
        self.assertEqual(1, len(self.room.livingspaces))
        self.assertEqual(1, len(self.room.offices))

        """Validates that duplicate rooms are not added"""
        self.room.create_room({
            "<room_name>": ["Office1"],
            "Living": False,
            "Office": True
        })
        # Duplicate rooms not added to any list
        self.assertEqual(2, len(self.room.rooms))
        self.assertEqual(1, len(self.room.offices))

    def test_office_has_capacity_of_6(self):
        """Ensure office has a capacity of 6"""
        office = Office()
        self.assertEqual(6, office.max_occupancy)

    def test_livingspace_has_capacity_of_4(self):
        livingspace = LivingSpace()
        self.assertEqual(4, livingspace.max_occupancy)
        """Ensure livingspace has a capacity of 4"""

    def test_print_room():
        """Tests for the print_room function"""
        pass

    def test_add_person(self):
        """Test addition of people"""
        #  Check if people added in setup
        self.assertEqual(2, len(self.person.people))
        self.assertEqual(1, len(self.person.fellows))
        self.assertEqual(1, len(self.person.staff))

        """Test if those who want accomodation are assigned rooms"""
        # Ensure that these people have been appended to rooms' occupants
        self.assertEqual(2, len(self.office1.occupants),
                         msg="Newly added people should \n"
                         "be added to room occupants")

    def test_add_fellow_with_accomodation(self):
        pass

    def test_rellocate_person(self):
        """Tests the relocation of people"""
        # Add a new office and assign it to a variable
        self.create_room({
            "<room_name>": ["Office2"],
            "Living": False,
            "Office": True
        })
        self.office2 = self.amity.offices[1]

        """Test the reallocation of Random Staff to office 2 from office 1"""
        self.reallocate_person({
            "<person_id>": int(self.randomstaff.person_id),
            "<new_room>": "Office2",
        })
        office2 = self.amity.offices[1]
        # Test that Random Staff now occupies Office2
        self.assertEqual(1, len(self.office2.occupants))
        self.assertEqual("Random Staff", self.office2.occupants[0],
                         msg="Occupant not added to list of occupants")

        # Test that Random Staff no longer in Office1 occupants
        self.assertEqual(0, len(self.office1.occupants))


if __name__ == '__main__':
    unittest.main()
