"""Constructor exercise."""


class Empty:
    """An empty class without constructor."""

    pass


class Person:
    """Represent person with firstname, lastname and age."""

    def __init__(self):
        self.firstname = ""
        self.lastname = ""
        self.age = 0


class Student:
    """Represent student with firstname, lastname and age."""

    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age 


if __name__ == '__main__':
    # empty class usage
    empty_instance = Empty()

    # Person class usage
    person_instance = Person("John", "Doe", 30)

    # Student class usage
    Student_instance = Student("Jane", "Doe", 25)
