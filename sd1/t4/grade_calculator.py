from typing import List


class GradeCalculator:

    def calculateAverage(self, grade: List[int]) -> float:
        if len(grade) == 0:
            return 0
        if any(type(grade) != int for grade in grade):
            raise ValueError("Grades must be integers")
        if any(grade < 0 for grade in grade):
            raise ValueError("Grades cannot be negative")
        return sum(grade) / len(grade)
