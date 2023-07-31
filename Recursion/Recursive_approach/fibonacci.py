def fibonacci_recursive(n):
    """
    Generate the nth Fibonacci number using recursion.

    Parameters:
    n (int): The position of the desired Fibonacci number (0-based indexing).

    Returns:
    int: The nth Fibonacci number.
    
    Raises:
    ValueError: If the input is a negative integer.
    """
    if n < 0:
        raise ValueError("Fibonacci sequence is not defined for negative indices.")
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

