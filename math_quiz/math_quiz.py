# import random module
import random


def integer(min_value, max_value):
    """
    Generate a random interger between the maximum and minimum values.

    Parameters:
    - min_value (int): The minimum value for the random integer.
    - max_value (int): The maximum value for the random integer.

    Returns:
    int: A random integer within the specified range.
    """
    # Use the random.randint to generate a random integer from the specified range
    return random.randint(min_value, max_value)


def operator():
    """
    Generate a random arithmatic operator: '+' , '-' , '*'

    Returns:
    str: A randomly selected arithmetic operator.
    """
    # use random.choice to select random operator from the list
    return random.choice(['+', '-', '*'])


def calculate_answer(a1, a2, operator):
    """
    Calculate answer on the base of operator 
    
    Parameters:
    - operand1 (int): The first operand in the arithmetic operation.
    - operand2 (int): The second operand in the arithmetic operation.
    - operator (str): The arithmetic operator ('+', '-', or '*').

    Returns:
    int: The result of the arithmetic operation.
    """
     # perform calculation on the of operator
    if operator == '+':
        return a1 + a2
    elif operator == '-':
        return a1 - a2
    else:
        return a1 * a2

def math_quiz():
    # initialize the score to 0 and set the total number of questions
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    # Loop through the specified number of total questions
    for _ in range(total_questions):
        for _ in range(total_questions):
         # generate random operands and operator
         a1 = integer(1, 10)
         a2 = integer(1, 5)
         operator = operator()

        # calculating answer for the current question
        PROBLEM, answer = calculate_answer(a1, a2, operator)
        print(f"\nQuestion: {PROBLEM}")
        user_answer = input("Your answer: ")

        # handling invalid input
        try:
            user_answer = int(user_answer)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue

        # checking whether the user answer is correct
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")
    
    # print the final score

    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    # tart the math quiz when the code executed
    math_quiz()
