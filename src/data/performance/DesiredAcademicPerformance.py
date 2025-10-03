import AcademicPerformance
from src.data.subject.Subject import Subject


class DesiredAcademicPerformance(AcademicPerformance):
    """
        The desired academic performance of a student. The grades here are not
        the ones given out by the teachers but rather the ones that students
        want to have.
    """

    def __init__(self, desired_subject_scores: dict[Subject, int]):
        self.__desired_subject_scores = desired_subject_scores

    def average_score(self) -> float:
        return sum(self.get_subject_scores().values()) / len(self._subject_scores.len())

    def __repr__(self):
        return (
            f"DesiredAcademicPerformance(subject_scores={self._subject_scores})",
            f"desired_average_score={self.average_score()}",
        )
