# SecureGrade

SecureGrade is a Python application designed to securely manage, validate, and calculate grades with additional features to convert numerical grades to letter grades and compute GPA on a 4.0 scale.

## Features

- **Grade Collection**: Collects grades from user input with validation to ensure grades are within a 0-100 range.
- **Average Calculation**: Calculates the average grade from the inputs.
- **Letter Grade Conversion**: Converts the average grade to a corresponding letter grade.
- **GPA Calculation**: Computes the GPA on a 4.0 scale based on the average grade.
- **Error Handling**: Provides error handling and logging to enhance security and user-friendliness.
- **Demo and Unit Tests**: Includes a demo for showcasing functionality and a test suite for verifying code correctness.

## Project Structure

- **grade_manager.py**: Contains the `GradeManager` class for managing grade operations, including input validation, averaging, letter grade conversion, and GPA calculation.
- **main.py**: Contains the `GradeApp` class, which serves as the main entry point for running the application.
- **demo.py**: A demonstration script that simulates grade inputs and displays the results, allowing users to see the application in action.
- **test_grade_manager.py**: Unit tests for the `GradeManager` class to verify that all functionalities work as expected.
- **requirements.txt**: Lists dependencies (currently none, but can be updated if external packages are added).
- **.gitignore**: Specifies files and folders to exclude from version control.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/SecureGrade.git
    cd SecureGrade
    ```

2. Install required packages (if any are added in the future):

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To run the program:

```bash
python main.py
```
# Demo

To see a demonstration of SecureGrade's functionality without manual input, run:

```bash
python demo.py
```
This will simulate inputting grades and display calculated averages, letter grades, and GPA.

#Testing
```bash
python -m inittest test_grade_manager.py
```

The tests cover grade addition, average calculation, letter grade conversion, and GPA conversion.
