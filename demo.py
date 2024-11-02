# Author: William Richmond
# Date: 2024-11-02
# Class: CYBR-260-45
# Assignment: SecureGrade Demo
# Description: Demonstrates the functionality of SecureGrade by simulating grade inputs and displaying results.

from grade_manager import GradeManager

def run_demo():
    """Runs a demonstration of the GradeManager functionality."""

    manager = GradeManager()

    # Demo for a fixed set of grades
    print("Demo: Fixed set of 6 grades [85, 90, 78, 92, 88, 95]")
    demo_grades = [85, 90, 78, 92, 88, 95]
    for grade in demo_grades:
        manager.add_grade(grade)
    average = manager.calculate_average()
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {manager.get_letter_grade(average)}")
    print(f"GPA: {manager.convert_to_gpa(average):.2f}")
    print()

    # Demo for a different set of grades
    print("Demo: Variable set of grades [73, 85, 91, 67, 89]")
    manager.clear_grades()
    demo_grades2 = [73, 85, 91, 67, 89]
    for grade in demo_grades2:
        manager.add_grade(grade)
    average = manager.calculate_average()
    print(f"Average: {average:.2f}")
    print(f"Letter Grade: {manager.get_letter_grade(average)}")
    print(f"GPA: {manager.convert_to_gpa(average):.2f}")

if __name__ == "__main__":
    run_demo()
