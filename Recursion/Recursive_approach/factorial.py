def factorial_recursive(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): Non-negative integer for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given integer.
    
    Raises:
    ValueError: If the input is a negative integer.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)

print(factorial_recursive(5))
