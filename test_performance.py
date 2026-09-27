import unittest
from performance import calculate_percentage, calculate_grade, calculate_result


class TestStudentPerformance(unittest.TestCase):

    def test_percentage(self):
        marks = [80, 90, 70, 60]
        result = calculate_percentage(marks)

        self.assertEqual(result, 75)

    def test_grade_a_plus(self):
        self.assertEqual(calculate_grade(95), "A+")

    def test_grade_a(self):
        self.assertEqual(calculate_grade(85), "A")

    def test_grade_b(self):
        self.assertEqual(calculate_grade(75), "B")

    def test_grade_c(self):
        self.assertEqual(calculate_grade(65), "C")

    def test_grade_d(self):
        self.assertEqual(calculate_grade(55), "D")

    def test_grade_f(self):
        self.assertEqual(calculate_grade(40), "F")

    def test_complete_result(self):
        marks = [85, 78, 92, 80]

        percentage, grade = calculate_result(marks)

        self.assertEqual(percentage, 83.75)
        self.assertEqual(grade, "A")


if __name__ == "__main__":
    unittest.main()