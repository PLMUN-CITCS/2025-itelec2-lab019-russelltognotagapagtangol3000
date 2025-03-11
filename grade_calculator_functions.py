"""Grade Calculator Program

This script prompts the user for a score, determines the corresponding letter grade,
and displays the result. It follows best practices including function decomposition,
input validation, and proper documentation.
"""


def get_student_score() -> float:
    """
    Prompts the user to enter their score, validates input, and returns the score as a float.
    
    Returns:
        float: The numerical score entered by the user.
    """
    while True:
        try:
            score = float(input("Enter your score: "))
            if 0 <= score <= 100:
                return score
            print("Error: Please enter a valid score between 0 and 100.")
        except ValueError:
            print("Error: Invalid input. Please enter a numerical value.")


def calculate_grade(score: float) -> str:
    """
    Determines the letter grade based on the given score using standard grading scale.
    
    Args:
        score (float): The numerical score to evaluate.
    
    Returns:
        str: The corresponding letter grade ('A', 'B', 'C', 'D', or 'F').
    """
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def main() -> None:
    """Main function that runs the grade calculator program."""
    score = get_student_score()
    grade = calculate_grade(score)
    print(f"Your Grade is: {grade}")


if __name__ == "__main__":
    main()
