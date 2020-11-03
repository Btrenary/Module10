""" Person class using property"""


class Person:
    """Person class"""
    TITLES = ('Dr', 'Mr', 'Mrs', 'Ms')

    def __init__(self, pid, title, name=''):  # Constructor
        self.person_id = pid
        self.title = title
        self.name = name
        print('Starting my constructor')

    @property
    def person_id(self):
        return self._person_id

    @person_id.setter
    def person_id(self, value):
        if isinstance(value, int):
            self._person_id = value
        else:
            raise AttributeError("")

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value not in self.TITLES:
            raise ValueError("%s is not a valid title" % value)
        self._title = value

    @property
    def name(self):
        print('getting my name')
        return self._name

    @name.setter
    def name(self, value):
        if value.isdigit():
            raise ValueError
        print('setting my name')
        self._name = value


# Driver
try:
    person = Person('Mr', 'Trenary')
except ValueError as err:
    print(err)
else:
    print(person.title + " " + person.name)
