from datetime import datetime

from src.CsvStudentDataWriter import CsvStudentDataWriter
from src.JsonStudentDataWriter import JsonStudentDataWriter
from src.data.AggregatedStudentInformation import AggregatedStudentInformation
from src.data.student.Student import Student
from src.data.subject.Subject import Subject

john_doe_information = AggregatedStudentInformation(
    student=Student("John Doe", "GRP-123", datetime(1990, 1, 1), "123 Main St"),
    subject_grades={
        Subject("Philosophy"): (5, 10),
        Subject("Maths"): (3, 6),
    }
)

print("John Doe information:", john_doe_information)

print("Writing a CSV file...")
CsvStudentDataWriter().write("john_doe_info", john_doe_information)

print("Writing a JSON file...")
JsonStudentDataWriter().write("john_doe_info", john_doe_information)

