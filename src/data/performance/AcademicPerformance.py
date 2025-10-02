from abc import ABC, abstractmethod


class AcademicPerformance(ABC):
    """
        Academic performance of a student.
    """

    @abstractmethod
    def average_score(self):
        pass
