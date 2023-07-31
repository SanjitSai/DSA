def factorial_iterative(n):
    """
    Calculate the factorial of a non-negative integer using iteration.

    Parameters:
    n (int): Non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given integer.
    
    Raises:
    ValueError: If the input is a negative integer.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
