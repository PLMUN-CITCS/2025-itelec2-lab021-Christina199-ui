def get_non_negative_integer() -> int:

    while True:
        try:
            user_input = input("Enter a non-negative integer: ")
            num = int(user_input)
            if num >= 0:
                return num
            else:
                print("Please enter a non-negative integer.")
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.")

def calculate_factorial(n: int) -> int:

    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def main():
    """
    Main program flow: gets user input, calculates factorial, and displays the result.
    """
    # Step 1: Get a valid non-negative integer from the user.
    number = get_non_negative_integer()

    # Step 2: Calculate the factorial of the number.
    result = calculate_factorial(number)

    # Step 3: Display the result.
    print(f"The factorial of {number} is: {result}")

if __name__ == "__main__":
    main()
