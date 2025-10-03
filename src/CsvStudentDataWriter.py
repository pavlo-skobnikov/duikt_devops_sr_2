import csv
from pathlib import Path

from src.data.AggregatedStudentInformation import AggregatedStudentInformation
from src.StudentDataWriter import StudentDataWriter


class CsvStudentDataWriter(StudentDataWriter):
    def write(self, file_name: str, data: AggregatedStudentInformation) -> None:
        path = Path(f"{file_name}.csv")
        student = data.get_student()
        subjects = data.get_subjects()
        actual_grades = data.get_actual_grades()
        desired_grades = data.get_desired_grades()
        actual_average = data.get_actual_average_grade()
        desired_average = data.get_desired_average_grade()

        with open(path, 'w', newline='') as file:
            writer = csv.writer(file)

            # Write header.
            header = [
                "full_name", "group_number", "birth_date", "address",
                "subject", "actual_grade", "desired_grade",
                "actual_average_grade", "desired_average_grade"
            ]
            writer.writerow(header)

            # Prepare student info.
            student_info = [
                student.get_full_name(),
                student.get_group_number(),
                student.get_birth_date().isoformat() if student.get_birth_date() else None,
                student.get_address(),
            ]

            summary_info = [actual_average, desired_average]

            # Write a row for each subject.
            for subject, actual, desired in zip(subjects, actual_grades, desired_grades):
                performance_info = [subject.get_name(), actual, desired]
                writer.writerow(student_info + performance_info + summary_info)
