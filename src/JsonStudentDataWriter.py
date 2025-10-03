import json
from pathlib import Path

from src.data.AggregatedStudentInformation import AggregatedStudentInformation
from src.StudentDataWriter import StudentDataWriter


class JsonStudentDataWriter(StudentDataWriter):
    def write(self, file_name: str, data: AggregatedStudentInformation) -> None:
        path = Path(f"{file_name}.json")
        student = data.get_student()
        subjects = data.get_subjects()
        actual_grades = data.get_actual_grades()
        desired_grades = data.get_desired_grades()

        output_data = {
            "student": {
                "full_name": student.get_full_name(),
                "group_number": student.get_group_number(),
                "birth_date": student.get_birth_date().isoformat() if student.get_birth_date() else None,
                "address": student.get_address(),
            },
            "performance": [
                {
                    "subject": subject.get_name(),
                    "actual_grade": actual,
                    "desired_grade": desired,
                }
                for subject, actual, desired in zip(subjects, actual_grades, desired_grades)
            ],
            "summary": {
                "actual_average_grade": data.get_actual_average_grade(),
                "desired_average_grade": data.get_desired_average_grade(),
            }
        }

        with open(path, 'w') as file:
            json.dump(output_data, file, indent=4)
