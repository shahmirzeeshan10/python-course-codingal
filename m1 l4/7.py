def fibonacci_sequence(n_terms):
    """
    Generate a list containing the Fibonacci sequence up to n_terms.
    :param n_terms: Number of terms to generate (must be >= 0)
    :return: List of Fibonacci numbers
    """
    if n_terms <= 0:
        return []  # No terms for zero or negative input
    elif n_terms == 1:
        return [0]
    elif n_terms == 2:
        return [0, 1]

    sequence = [0, 1]
    for _ in range(2, n_terms):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence


if __name__ == "__main__":
    try:
        # Get user input
        n = int(input("Enter the number of Fibonacci terms to generate: "))

        # Validate input
        if n < 0:
            print("Please enter a non-negative integer.")
        else:
            result = fibonacci_sequence(n)
            print(f"Fibonacci sequence with {n} terms:")
            print(result)

    except ValueError:
        print("Invalid input. Please enter an integer.")
How it works:
Function fibonacci_sequence(n_terms)
Handles cases for 0, 1, and 2 terms separately.
Uses a loop to build the sequence for n_terms > 2.
Input Validation
Ensures the user enters a non-negative integer.
Edge Cases
n = 0 → returns []
n = 1 → returns [0]
n = 2 → returns [0, 1]