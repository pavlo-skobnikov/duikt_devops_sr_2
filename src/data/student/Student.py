from datetime import date


class Student:
    """
        A student in an educational establishment.
    """

    def __init__(
            self,
            full_name: str,
            group_number: str,
            birth_date: date,
            address: str,
    ):
        self.__full_name = full_name
        self.__group_number = group_number
        self.__birth_date = birth_date
        self.__address = address

    def get_full_name(self) -> str:
        return self.__full_name

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def get_group_number(self) -> str:
        return self.__group_number

    def set_group_number(self, group_number):
        self.__group_number = group_number

    def get_birth_date(self) -> date | None:
        return self.__birth_date

    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def get_address(self) -> str | None:
        return self.__address

    def set_address(self, address):
        self.__address = address

    def __str__(self):
        return (
            f'Student(full_name={self.__full_name}, '
            f'group_number={self.__group_number}, '
            f'birth_date={self.__birth_date}, '
            f'address={self.__address})',
        )
