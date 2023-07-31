def fibonacci_iterative(n):
    """
    Generate the nth Fibonacci number using iteration.

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
    if n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
