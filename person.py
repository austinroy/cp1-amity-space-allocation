class Person(object):
    """Class containing attributes of all person types"""

    def __init__(self, name):
        self.name = name
        self.person_id = id(self)


class Fellow(Person):
    """Class containing attributes of Fellows"""
    person_title = "Fellow"

    def __init__(self, name):
        super(Fellow, self).__init__(name)


class Staff(Person):
    """Class containing attributes of Staff"""
    person_title = "Staff"

    def __init__(self, name):
        super(Staff, self).__init__(name)
