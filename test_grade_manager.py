# Author: William Richmond
# Date: 2024-11-02
# Class: CYBR-260-45
# Assignment: SecureGrade Unit Tests
# Description: Unit tests for GradeManager functions in SecureGrade using the unittest framework.

import unittest
from grade_manager import GradeManager

class TestGradeManager(unittest.TestCase):
    """Unit tests for GradeManager class methods."""

    def setUp(self):
        """Set up a GradeManager instance for testing."""
        self.manager = GradeManager()

    # function: test_add_grade
    # purpose: Tests adding a grade to the manager
    # inputs: None
    # returns: None
    def test_add_grade(self):
        self.manager.add_grade(85)
        self.assertEqual(self.manager.grades, [85])

    # function: test_calculate_average
    # purpose: Tests calculating the average of grades
    # inputs: None
    # returns: None
    def test_calculate_average(self):
        grades = [85, 90, 78]
        for grade in grades:
            self.manager.add_grade(grade)
        self.assertAlmostEqual(self.manager.calculate_average(), 84.33, places=2)

    # function: test_get_letter_grade
    # purpose: Tests conversion from numerical grade to letter grade
    # inputs: None
    # returns: None
    def test_get_letter_grade(self):
        self.assertEqual(self.manager.get_letter_grade(95), "A")
        self.assertEqual(self.manager.get_letter_grade(67), "D+")
        self.assertEqual(self.manager.get_letter_grade(59), "F")

    # function: test_convert_to_gpa
    # purpose: Tests conversion from numerical grade to GPA on a 4.0 scale
    # inputs: None
    # returns: None
    def test_convert_to_gpa(self):
        self.assertEqual(self.manager.convert_to_gpa(95), 4.0)
        self.assertEqual(self.manager.convert_to_gpa(85), 3.0)
        self.assertEqual(self.manager.convert_to_gpa(70), 1.7)

    def tearDown(self):
        """Clear grades after each test."""
        self.manager.clear_grades()

if __name__ == "__main__":
    unittest.main()
