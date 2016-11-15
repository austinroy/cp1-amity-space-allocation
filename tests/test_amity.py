import unittest

from amity import Amity


class TestRoom(unittest.TestCase):
    """Unit tests to test functions in the Person Class"""

    def setUp(self):
        self.amity = Amity()

    def test_print_allocations(self):
        """Tests that allocations are printed"""
        pass

    def test_print_unallocated(self):
        """Tests that unallocated people are printed"""
        pass

    def test_load_people(self):
        """Tests loading of people from text file"""
        pass


if __name__ == '__main__':
    unittest.main()
