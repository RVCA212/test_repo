import math
import cmath
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def factorial_recursive(n):
    """Calculate factorial using recursion."""
    logger.info(f"Calculating factorial for n = {n}")
    if n < 0:
        logger.error(f"Factorial attempted with negative number: {n}")
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1 if n <= 1 else n * factorial_recursive(n-1)
    logger.info(f"Factorial of {n} is {result}")
    return result

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms."""
    logger.info(f"Generating Fibonacci sequence for {n} terms")
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    logger.debug(f"Generated Fibonacci sequence: {fib_seq[:n]}")
    return fib_seq[:n]

def complex_root(a, b, c):
    """
    Calculate and analyze complex roots of a quadratic equation ax^2 + bx + c = 0.
    
    Returns a dictionary with detailed root information:
    - roots: the calculated roots
    - type: nature of roots (real, complex, repeated)
    - sum_of_roots: sum of the roots
    - product_of_roots: product of the roots
    """
    logger.info(f"Calculating roots for quadratic equation: {a}x^2 + {b}x + {c} = 0")
    
    # Handle special cases
    if a == 0:
        logger.error("Coefficient 'a' cannot be zero in a quadratic equation")
        raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation")
    
    # Calculate discriminant
    discriminant = b**2 - 4*a*c
    logger.debug(f"Discriminant calculated: {discriminant}")
    
    # Compute roots
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        root_type = "real_distinct"
        logger.info(f"Two distinct real roots found: {root1}, {root2}")
    elif discriminant == 0:
        # One repeated real root
        root1 = root2 = -b / (2*a)
        root_type = "real_repeated"
        logger.info(f"One repeated real root found: {root1}")
    else:
        # Complex conjugate roots
        root1 = complex(-b / (2*a), math.sqrt(abs(discriminant)) / (2*a))
        root2 = complex(-b / (2*a), -math.sqrt(abs(discriminant)) / (2*a))
        root_type = "complex_conjugate"
        logger.info(f"Complex conjugate roots found: {root1}, {root2}")
    
    result = {
        "roots": (root1, root2),
        "type": root_type,
        "sum_of_roots": root1 + root2,
        "product_of_roots": root1 * root2,
        "equation": f"{a}x^2 + {b}x + {c} = 0"
    }
    logger.debug(f"Full root analysis result: {result}")
    return result