from abc import ABC, abstractmethod

from src.data.AggregatedStudentInformation import AggregatedStudentInformation


class StudentDataWriter(ABC):
    @abstractmethod
    def write(self, file_name: str, data: AggregatedStudentInformation) -> None:
        pass
