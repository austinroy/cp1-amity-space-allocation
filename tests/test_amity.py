import unittest

from amity import Amity


class TestRoom(unittest.TestCase):
    """Unit tests to test functions in the Person Class"""

    def setUp(self):
        self.amity = Amity()

    def test_print_allocations(self):
        pass

    def test_print_unallocated(self):
        pass

    def test_load_people(self):
        pass


if __name__ == '__main__':
    unittest.main()
