import unittest

from person import Person, Fellow, Staff

from room import Room


class TestPerson(unittest.TestCase):
    """Unit tests to test functions in the Person Class"""

    def setUp(self):
        self.person = Person()

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
        self.office1 = self.test_amity.offices[0]

    def test_add_person(self):
        """Test addition of people"""
        #  Check if people added in setup
        self.assertEqual(2, len(self.person.people))
        self.assertEqual(1, len(self.person.fellows))
        self.assertEqual(1, len(self.person.staff))

        """Test if those who want accomodation are assigned rooms"""
        # Ensure that these people have been appended to rooms' occupants
        self.assertEqual(2, len(self.office1.occupants))

    def test_fellow_subclass_of_person(self):
        """Tests if class Fellow is a subclass of class Person"""
        self.assertTrue((issubclass(Fellow, Person)),
                        msg='Class Fellow should be a subclass of Person')

    def test_staff_subclass_of_person(self):
        """Tests if class Staff is a subclass of class Person"""
        self.assertTrue((issubclass(Staff, Person)),
                        msg='Class Staff should be a subclass of Person')

    def test_person_is_fellow_or_staff(self):
        """Validates that the person added has a title of either fellow or staff
         and nothing other than those two"""
        self.assertTrue((
                        self.person.person_title == "Fellow" or
                        self.person.person_title == "Staff"),
                        msg="person_title should be either Fellow or Staff")

    def test_staff_not_given_livingspace(self):
        """Validates staff are not given living space"""
        self.assertEqual()
        pass

    def test_fellow_given_accomodation_option(self):
        """Validates felows have the option for accomodation"""
        pass


if __name__ == '__main__':
    unittest.main()
