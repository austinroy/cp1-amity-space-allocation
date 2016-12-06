class Person(object):
    """docstring for Person"""
    person_id = 1

    def __init__(self, name):
        self.name = name


class Fellow(Person):
    """docstring for Fellow"""

    def __init__(self, name):
        self.name = name
        self.person_title = "Fellow"


class Staff(Person):
    """docstring for Staff"""

    def __init__(self, name):
        self.name = name
        self.person_title = "Staff"