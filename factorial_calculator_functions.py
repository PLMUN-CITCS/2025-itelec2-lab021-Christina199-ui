def get_non_negative_integer() -> int:
    """
    Prompts the user to input a non-negative integer.

    This function will repeatedly ask the user for an input until a valid 
    non-negative integer (0 or greater) is entered. If the input is invalid,
    an error message is displayed, and the user is asked again.

    Returns:
        int: A valid non-negative integer entered by the user.
    """
    while True:
        try:
            # Prompt user to enter a non-negative integer
            user_input = input("Enter a non-negative integer: ")

            # Convert input to integer
            num = int(user_input)

            # Check if the number is non-negative
            if num >= 0:
                return num
            else:
                print("Please enter a non-negative integer.")  # Error message for negative input
        except ValueError:
            # Catch ValueError when input cannot be converted to an integer
            print("Invalid input. Please enter a valid non-negative integer.")  # Error message for non-integer input

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a given non-negative integer.

    The factorial of a number n is the product of all positive integers 
    less than or equal to n. The factorial of 0 is defined as 1.

    Args:
        n (int): The non-negative integer for which the factorial is calculated.

    Returns:
        int: The factorial of the given number.
    
    Example:
        calculate_factorial(5) -> 120
    """
    factorial = 1  # Initialize factorial to 1 (base case for multiplication)
    
    # Multiply all integers from 1 to n to calculate the factorial
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial  # Return the computed factorial

def main():
    """
    Main program flow: 
    1. Gets user input for a non-negative integer.
    2. Calculates the factorial of the integer.
    3. Displays the result to the user.
    
    This function serves as the entry point to the program and coordinates 
    the calls to the other functions to accomplish the program's task.
    """
    # Step 1: Get a valid non-negative integer from the user.
    number = get_non_negative_integer()

    # Step 2: Calculate the factorial of the number.
    result = calculate_factorial(number)

    # Step 3: Display the result to the user.
    print(f"The factorial of {number} is: {result}")

# Run the program when executed directly
if __name__ == "__main__":
    main()
