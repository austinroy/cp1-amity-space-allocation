import unittest

from person import Person


class TestPerson(unittest.Testcase):
	"""Unit tests to test functions in the Person Class"""

	def setUp (self):
		self.person = Person ()

	def test_add_person (self):
		""" Tests the add person function"""
		pass

	def test_rellocate_person(self):
		"""Tests rellocation function"""
		pass

	def test_fellow_subclass_of_person(self):
		"""Tests if class Fellow is a subclass of class Person"""
		self.asserTrue((issubclass(Fellow,Person)),
						 msg='Class Fellow should be a subclass of Person')

	def test_staff_subclass_of_person(self):
		"""Tests if class Staff is a subclass of class Person"""
		self.asserTrue((issubclass(Staff,Person)),
						 msg='Class Staff should be a subclass of Person')

if __name__ = '__main__':
	unittest.main()
