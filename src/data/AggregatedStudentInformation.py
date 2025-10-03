from src.data.performance.ActualAcademicPerformance import ActualAcademicPerformance
from src.data.performance.DesiredAcademicPerformance import DesiredAcademicPerformance
from src.data.student.Student import Student
from src.data.subject.Subject import Subject


class AggregatedStudentInformation:
    """
        Aggregated information about a student, including their personal
        information, academic performance, and desired academic performance.
    """

    def __init__(
            self,
            student: Student,
            subject_grades: dict[Subject, tuple[int, int]],
    ):
        """
            NOTE: The `subject_grades` is a dictionary where the key is the
            subject and the value is a tuple of the actual grade and the
            student's desired grade.
        """
        self.__student = student
        self.__subjects = [subject for subject in subject_grades.keys()]
        self.__actual_grades = [grade[0] for grade in subject_grades.values()]
        self.__actual_academic_performance = ActualAcademicPerformance(
            {subject: grade[0] for subject, grade in subject_grades.items()},
        )
        self.__desired_grades = [grade[1] for grade in subject_grades.values()]
        self.__desired_academic_performance = DesiredAcademicPerformance(
            {subject: grade[1] for subject, grade in subject_grades.items()},
        )

    def get_student(self) -> Student:
        return self.__student

    def get_subjects(self) -> list[Subject]:
        return self.__subjects

    def get_actual_grades(self) -> list[int]:
        return self.__actual_grades

    def get_actual_average_grade(self) -> float:
        return self.__actual_academic_performance.average_score()

    def get_desired_grades(self) -> list[int]:
        return self.__desired_grades

    def get_desired_average_grade(self) -> float:
        return self.__desired_academic_performance.average_score()
