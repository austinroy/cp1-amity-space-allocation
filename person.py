class Person(object):
    """docstring for Person"""


class Fellow(Person):
    """docstring for Fellow"""

    def __init__(self, name):
        self.name = name
        self.person_title = "Fellow"
        self.person_id = id(self)


class Staff(Person):
    """docstring for Staff"""

    def __init__(self, name):
        self.name = name
        self.person_title = "Staff"
        self.person_id = id(self)
