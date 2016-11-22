import unittest

from person import Person, Fellow, Staff

from room import Room


class TestPerson(unittest.TestCase):
    """Unit tests to test functions in the Person Class"""

    def setUp(self):
        self.person = Person()

    def test_add_person(self):
        """Test addition of people"""
        #  Check if people added in setup
        self.assertEqual(2, len(self.person.people))
        self.assertEqual(1, len(self.person.fellows))
        self.assertEqual(1, len(self.person.staff))

        """Test if those who want accomodation are assigned rooms"""
        # Ensure that these people have been appended to rooms' occupants
        self.assertEqual(2, len(self.office1.occupants))

    def test_person_is_fellow_or_staff(self):
        """Validates that the person added has a title of either fellow or staff
         and nothing other than those two"""
        self.assertTrue((
                        self.person.person_title == "Fellow" or
                        self.person.person_title == "Staff"),
                        msg="person_title should be either Fellow or Staff")


if __name__ == '__main__':
    unittest.main()
