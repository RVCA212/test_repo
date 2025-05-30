import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

import math
import cmath
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def factorial_recursive(n):
    """Calculate factorial using recursion."""
    try:
        logger.info(f"Calculating factorial for n = {n}")
        if n < 0:
            logger.error(f"Invalid input: Factorial not defined for negative number {n}")
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1 if n <= 1 else n * factorial_recursive(n-1)
        logger.info(f"Factorial of {n} is {result}")
        return result
    except Exception as e:
        logger.exception(f"Error in factorial calculation: {e}")
        raise

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms."""
    try:
        logger.info(f"Generating Fibonacci sequence with {n} terms")
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        logger.info(f"Generated Fibonacci sequence: {fib_seq[:n]}")
        return fib_seq[:n]
    except Exception as e:
        logger.exception(f"Error generating Fibonacci sequence: {e}")
        raise

def complex_root(a, b, c):
    """Calculate and analyze complex roots of a quadratic equation."""
    try:
        logger.info(f"Calculating roots for equation: {a}x^2 + {b}x + {c} = 0")
        if a == 0:
            logger.error("Coefficient 'a' cannot be zero in a quadratic equation")
            raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation")
        
        discriminant = b**2 - 4*a*c
        logger.debug(f"Discriminant: {discriminant}")
        
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            root_type = "real_distinct"
        elif discriminant == 0:
            root1 = root2 = -b / (2*a)
            root_type = "real_repeated"
        else:
            root1 = complex(-b / (2*a), math.sqrt(abs(discriminant)) / (2*a))
            root2 = complex(-b / (2*a), -math.sqrt(abs(discriminant)) / (2*a))
            root_type = "complex_conjugate"
        
        result = {
            "roots": (root1, root2),
            "type": root_type,
            "sum_of_roots": root1 + root2,
            "product_of_roots": root1 * root2,
            "equation": f"{a}x^2 + {b}x + {c} = 0"
        }
        logger.info(f"Roots: {result['roots']}, Type: {result['type']}")
        return result
    except Exception as e:
        logger.exception(f"Error calculating roots: {e}")
        raise