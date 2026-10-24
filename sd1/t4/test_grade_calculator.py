import pytest

from grade_calculator import GradeCalculator


def test_calculate_average():
    calculator = GradeCalculator()
    assert calculator.calculateAverage([1, 2, 3, 4, 5]) == 3


def test_calculate_average_empty_list():
    calculator = GradeCalculator()
    assert calculator.calculateAverage([]) == 0


def test_calculate_average_non_integer_grades():
    calculator = GradeCalculator()
    assert pytest.raises(ValueError, calculator.calculateAverage, [1, '2', 3, 4, 5])


def test_calculate_average_one_grade():
    calculator = GradeCalculator()
    assert calculator.calculateAverage([1]) == 1


def test_calculate_average_negative_grades():
    calculator = GradeCalculator()
    assert pytest.raises(ValueError, calculator.calculateAverage, [-1, -2, -3, -4, -5])


def test_calculate_average_zero_grades():
    calculator = GradeCalculator()
    assert calculator.calculateAverage([0, 0, 0, 0, 0]) == 0

def test_calculate_non_int_result():
    calculator = GradeCalculator()
    assert calculator.calculateAverage([1, 2]) == 1.5

def test_calculate_with_zero_grades():
    calculator = GradeCalculator()
    assert calculator.calculateAverage([0, 10]) == 5.0