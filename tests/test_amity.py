import unittest

from amity import Amity


class TestRoom(unittest.TestCase):
    """Unit tests to test functions in the Person Class"""

    def setUp(self):
        self.amity = Amity()

    def test_print_allocations():
        pass

    def test_print_unallocated():
        pass

    def test_load_people():
        pass


if __name__ == '__main__':
    unittest.main()
