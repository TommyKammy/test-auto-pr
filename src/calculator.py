"""
Simple Calculator Module

This module provides basic arithmetic operations.
TODO: Add more advanced operations
"""

def add(a, b):
    """Add two numbers."""
    return a + b

def subtract(a, b):
    """Subtract b from a."""
    return a - b

def multiply(a, b):
    """Multiply two numbers."""
    return a * b

def divide(a, b):
    """Divide a by b."""
    # TODO: Add error handling for division by zero
    return a / b

def power(base, exponent):
    """Calculate base raised to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent (must be non-negative)
    
    Returns:
        base ** exponent
    
    Raises:
        ValueError: If exponent is negative
    """
    if exponent < 0:
        raise ValueError("Exponent must be non-negative")
    return base ** exponent

def sqrt(n):
    """Calculate the square root of a number.
    
    Args:
        n: The number to calculate square root for
    
    Returns:
        The square root of n
    
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Cannot calculate square root of negative number")
    import math
    return math.sqrt(n)
