"""Encapsulation exercise."""


class Student:
    """Represent student with name, id and status."""

    def __init__(self, name, id):
        """Initialize a new student object.

        Args:
            name: The student's name.
            id: The student's ID.
        """
        self.__name = name
        self.__id = id  # ID is private and should not be directly accessed.
        self.__status = "Active"  # Status is also private and should not be directly accessed.

    def get_id(self):
        """Get the student's ID.

        Returns:
            The student's ID.
        """
        return self.__id

    def set_name(self, name):
        """Set the student's name.

        Args:
            name: The new name for the student.
        """
        self.__name = name

    def get_name(self):
        """Get the student's name.

        Returns:
            The student's name.
        """
        return self.__name

    def set_status(self, status):
        """Set the student's status.

        Args:
            status: The new status for the student.
        """
        valid_statuses = {"Active", "Expelled", "Finished", "Inactive"}
        if status in valid_statuses:
            self.__status = status

    def get_status(self):
        """Get the student's status.

        Returns:
            The student's status.
        """
        return self.__status


if __name__ == "__main__":
    student = Student("John Doe", 12345)
    print(student.get_id())  # 12345
    print(student.get_name())  # John Doe
    student.set_name("Jane Doe")
    print(student.get_name())  # Jane Doe
    student.set_status("Expelled")
    print(student.get_status())  # Expelled
    student.set_status("Invalid")
    print(student.get_status())  # Expelled

    pass