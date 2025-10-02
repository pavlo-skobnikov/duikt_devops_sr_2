class Subject:
    """
       A subject in an educational establishment.
    """

    def __init__(self, name: str):
        self.__name = name

    def get_name(self) -> str:
        return self.__name

    def __repr__(self):
        return f"Subject(name={self.__name})"
