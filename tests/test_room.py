import unittest

from room import Room, Office, LivingSpace


class TestRoom(unittest.TestCase):
    """Unit tests to test functions in the Person Class"""

    def setUp(self):
        self.room = Room()

    def test_create_room(self):
        """Tests room creation"""
        pass

    def test_print_room(self):
        """Test if printing of rooms and their occupants"""
        pass

    def test_office_subclass_of_room(self):
        """Tests if class Office is a subclass of class Room"""
        self.assertTrue((issubclass(Office, Room)),
                        msg='Class Office should be a subclass of Room')

    def test_livingspace_subclass_of_room(self):
        """Tests if class LivingSpace is a subclass of Room"""
        self.assertTrue((issubclass(LivingSpace, Room)),
                        msg='Class LivingSpace should be a subclass of Room')


if __name__ == '__main__':
    unittest.main()
