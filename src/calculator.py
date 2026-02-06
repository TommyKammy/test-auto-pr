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

# TODO: Add square root function
# def sqrt(n):
#     pass
