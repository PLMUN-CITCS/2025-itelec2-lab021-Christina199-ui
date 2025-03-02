def get_non_negative_integer() -> int:
    """
    Asks the user for a non-negative integer.

    Continues until a valid input (0 or greater) is entered.
    """
    while True:
        try:
            num = int(input("Enter a non-negative integer: "))
            if num >= 0:
                return num
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculate_factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer.
    
    The factorial of n is the product of all whole numbers from 1 to n.
    For example, factorial(5) = 5 * 4 * 3 * 2 * 1 = 120. 
    Factorial of 0 is 1.

    Args:
        n (int): The non-negative integer for which the factorial is calculated.

    Returns:
        int: The factorial of the input number n.
        
    Example:
        calculate_factorial(5) -> 120
    """
    factorial = 1  # Start with 1 (since factorial of 0 is 1)
    
    # Loop to multiply each integer from 1 to n
    for i in range(1, n + 1):
        factorial *= i
    
    return factorial  # Return the calculated factorial

def main():
    """
    Main program: gets user input, calculates the factorial, and shows the result.
    
    It asks for a valid number, calculates its factorial, and prints the result.
    """
    # Get a valid non-negative integer from the user.
    number = get_non_negative_integer()

    # Calculate the factorial of the entered number.
    result = calculate_factorial(number)

    # Display the result.
    print(f"The factorial of {number} is: {result}")

if __name__ == "__main__":
    main()
