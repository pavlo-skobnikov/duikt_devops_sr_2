import AcademicPerformance
from src.data.subject.Subject import Subject


class ActualAcademicPerformance(AcademicPerformance):
    """
        The actual academic performance of a student based on the grades
        received per subject.
    """

    def __init__(self, actual_subject_scores: dict[Subject, int]):
        self.__actual_subject_scores = actual_subject_scores

    def average_score(self) -> float:
        return sum(self.get_subject_scores().values()) / len(self._subject_scores.len())

    def __repr__(self):
        return (
            f"ActualAcademicPerformance(subject_scores={self._subject_scores})",
            f"actual_average_score={self.average_score()}",
        )
