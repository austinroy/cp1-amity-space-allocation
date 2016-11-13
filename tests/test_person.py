import unittest

from person import Person, Fellow, Staff


class TestPerson(unittest.TestCase):
    """Unit tests to test functions in the Person Class"""

    def setUp(self):
        self.person = Person()

    def test_add_person(self):
        """ Tests the add person function"""
        pass

    def test_rellocate_person(self):
        """Tests rellocation function"""
        pass

    def test_fellow_subclass_of_person(self):
        """Tests if class Fellow is a subclass of class Person"""
        self.assertTrue((issubclass(Fellow, Person)),
                        msg='Class Fellow should be a subclass of Person')

    def test_staff_subclass_of_person(self):
        """Tests if class Staff is a subclass of class Person"""
        self.assertTrue((issubclass(Staff, Person)),
                        msg='Class Staff should be a subclass of Person')


class TestAddPerson(unittest.TestCase):
    """Tests the validity of the add_person function"""
    # def __init__(self, arg):
    #     super(TestAddPerson, self).__init__()
    #     self.arg = arg

    def test_person_is_fellow_or_staff(self):
        """Validates that the person added has a title of either fellow or staff
         and nothing other than those two"""
        self.assertTrue((
                        person_title == "fellow" or
                        person_title == "staff"),
                        msg="person_title should be either fellow or staff")

    def test_staff_not_given_livingspace(self):
        pass


class TestRellocatePerson(object):
    """Tests validity of the rellocate_person function"""
    def __init__(self, arg):
        super(TestRellocatePerson, self).__init__()
        self.arg = arg


if __name__ == '__main__':
    unittest.main()
