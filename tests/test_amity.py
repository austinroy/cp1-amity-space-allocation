import unittest

from amity import Amity

from room import Office, LivingSpace


class TestRoom(unittest.TestCase):
    """Unit tests to test functions in the Person Class"""

    def setUp(self):
        self.amity = Amity()

        self.amity.create_room({
            "<room_name>": ["LivingSpace1"],
            "Living": True,
            "Office": False
        })
        """Create sample living space"""
        self.amity.create_room({
            "<room_name>": ["Office1"],
            "Living": False,
            "Office": True
        })
        self.office1 = self.amity.offices[0]

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


if __name__ == '__main__':
    unittest.main()
