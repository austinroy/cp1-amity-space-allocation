import unittest

from room import Room


class TestRoom(unittest.Testcase):
	"""Unit tests to test functions in the Person Class"""

	def setUp (self):
		self.room = Room()

	def test_create_room (self):
		pass

	def test_print_room(self):
		pass
		


if __name__ = '__main__':
	unittest.main()
