# Author: William Richmond
# Date: 2024-11-02
# Class: CYBR-260-45
# Assignment: Grade Averaging App with Enhanced Security
# Description: This module initializes and runs the GradeApp with additional error handling and logging.

from grade_manager import GradeManager
import logging

logging.basicConfig(filename='grade_app.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

class GradeApp:
    """Main application to manage user interactions for grade averaging."""

    def __init__(self):
        """Initializes the GradeManager instance."""
        self.manager = GradeManager()

    # function: display_results
    # purpose: Calculates and displays average, letter grade, and GPA
    # inputs: None
    # returns: None
    def display_results(self):
        average = self.manager.calculate_average()
        letter_grade = self.manager.get_letter_grade(average)
        gpa = self.manager.convert_to_gpa(average)
        print(f"The average of the grades is: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")
        print(f"GPA on a 4.0 scale: {gpa:.1f}")

    # function: run_fixed_grades
    # purpose: Runs part one of the program with a fixed number of grades
    # inputs: None
    # returns: None
    def run_fixed_grades(self):
        print("Enter 6 grades for the first part:")
        self.manager.add_grades_from_input(6)
        self.display_results()
        self.manager.clear_grades()

    # function: run_variable_grades
    # purpose: Runs part two of the program with a variable number of grades and error handling for user input
    # inputs: None
    # returns: None
    def run_variable_grades(self):
        while True:
            try:
                num_grades = int(input("How many grades do you have? "))
                break
            except ValueError as e:
                logging.error(f"Invalid input for grade count: {e}")
                print("Invalid input. Please enter a valid integer.")

        print(f"Enter {num_grades} grades for the second part:")
        self.manager.add_grades_from_input(num_grades)
        self.display_results()
        self.manager.clear_grades()

    # function: main
    # purpose: Main method to run both parts of the program
    # inputs: None
    # returns: None
    def main(self):
        self.run_fixed_grades()
        self.run_variable_grades()

# Run the GradeApp if this is the main module
if __name__ == "__main__":
    app = GradeApp()
    app.main()
