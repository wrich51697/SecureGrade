# Author: William Richmond
# Date: 2024-11-02
# Class: CYBR-260-45
# Assignment: Modularized Grade Averaging Program with Enhanced Security
# Description: This module contains the GradeManager class with improved error handling and input validation.

import logging

# Set up logging to capture errors
logging.basicConfig(filename='grade_manager.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class GradeManager:
    """Handles operations related to managing grades."""
    MIN_GRADE = 0.0
    MAX_GRADE = 100.0

    def __init__(self):
        """Initializes an empty list of grades."""
        self.grades = []

    # function: add_grade
    # purpose: Adds a grade to the list and issues a warning if out of range
    # inputs: Grade (float)
    # returns: None
    def add_grade(self, grade):
        if grade < self.MIN_GRADE or grade > self.MAX_GRADE:
            print("Warning: Grade should be between 0 and 100.")
        self.grades.append(grade)

    # function: calculate_average
    # purpose: Calculates the average of grades
    # inputs: None
    # returns: Average grade (float)
    def calculate_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    # function: get_letter_grade
    # purpose: Converts a numerical grade to a letter grade
    # inputs: Numerical grade (float)
    # returns: Letter grade (str)
    def get_letter_grade(self, grade):
        if grade >= 97:
            return "A+"
        elif grade >= 93:
            return "A"
        elif grade >= 90:
            return "A-"
        elif grade >= 87:
            return "B+"
        elif grade >= 83:
            return "B"
        elif grade >= 80:
            return "B-"
        elif grade >= 77:
            return "C+"
        elif grade >= 73:
            return "C"
        elif grade >= 70:
            return "C-"
        elif grade >= 67:
            return "D+"
        elif grade >= 63:
            return "D"
        elif grade >= 60:
            return "D-"
        else:
            return "F"

    # function: convert_to_gpa
    # purpose: Converts a numerical grade to a 4.0 scale GPA
    # inputs: Numerical grade (float)
    # returns: GPA (float)
    def convert_to_gpa(self, grade):
        if grade >= 93:
            return 4.0
        elif grade >= 90:
            return 3.7
        elif grade >= 87:
            return 3.3
        elif grade >= 83:
            return 3.0
        elif grade >= 80:
            return 2.7
        elif grade >= 77:
            return 2.3
        elif grade >= 73:
            return 2.0
        elif grade >= 70:
            return 1.7
        elif grade >= 67:
            return 1.3
        elif grade >= 63:
            return 1.0
        elif grade >= 60:
            return 0.7
        else:
            return 0.0

    # function: clear_grades
    # purpose: Clears the list of grades
    # inputs: None
    # returns: None
    def clear_grades(self):
        self.grades.clear()

    # function: add_grades_from_input
    # purpose: Collects grades from user input and adds them to the list with error handling
    # inputs: Number of grades (int)
    # returns: None
    def add_grades_from_input(self, num_grades, max_retries=3):
        for i in range(num_grades):
            attempts = 0
            while attempts < max_retries:
                try:
                    grade = float(input(f"Enter grade {i + 1}: "))
                    self.add_grade(grade)
                    break  # Exit loop if successful
                except ValueError as e:
                    attempts += 1
                    logging.error(f"Invalid input: {e}")
                    print("Invalid input. Please enter a valid numeric grade.")
                if attempts == max_retries:
                    print("Max retries reached. Moving to the next grade.")
