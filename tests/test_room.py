import unittest

from room import Room, Office, LivingSpace


class TestRoom(unittest.TestCase):
    """Unit tests for the Room class"""

    def setUp(self):
        self.room = Room()

        self.room.create_room({
            "<room_name>": ["LivingSpace1"],
            "Living": True,
            "Office": False
        })
    """Create sample living space"""
        self.room.create_room({
            "<room_name>": ["Office1"],
            "Living": False,
            "Office": True
        })

        # Assign rooms to variables
        self.livinga = self.room.livingspaces[0]
        self.officea = self.room.offices[0]

    def test_office_subclass_of_room(self):
        """Tests if class Office is a subclass of class Room"""
        self.assertTrue((issubclass(Office, Room)),
                        msg='Class Office should be a subclass of Room')

    def test_livingspace_subclass_of_room(self):
        """Tests if class LivingSpace is a subclass of Room"""
        self.assertTrue((issubclass(LivingSpace, Room)),
                        msg='Class LivingSpace should be a subclass of Room')

    def test_create_room():
        """Test creation of rooms"""
        # LivingA and OfficeA from setup() added to relevant lists
        self.assertEqual(2, len(self.test_amity.rooms))
        self.assertEqual(1, len(self.test_amity.livingspaces))
        self.assertEqual(1, len(self.test_amity.offices))

    def test_room_has_a_unique_name(self):
        pass

    def function():
        pass


class TestPrintRoom(unittest.TestCase):
    """Tests for the print_room function"""


class TestOfficeStructure(unittest.TestCase):
    """Tests class Office structure"""

    def test_office_has_capacity_of_6(self):
        """Ensure office has a capacity of 6"""
        pass


class TestLvivngSpaceStructure(object):
    """Tests class Office structure"""

    def test_livingspace_has_capacity_of_4(self):
        """Ensure livingspace has a capacity of 4"""
        pass


if __name__ == '__main__':
    unittest.main()
