import math
import cmath
import logging
import os

# Configure logging
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'advanced_math.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def factorial_recursive(n):
    """Calculate factorial using recursion."""
    try:
        logger.info(f"Calculating factorial for n = {n}")
        if n < 0:
            logger.error(f"Factorial attempted with negative number: {n}")
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1 if n <= 1 else n * factorial_recursive(n-1)
        logger.info(f"Factorial of {n} is {result}")
        return result
    except Exception as e:
        logger.exception(f"Error in factorial_recursive: {e}")
        raise

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms."""
    try:
        logger.info(f"Generating Fibonacci sequence for {n} terms")
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        logger.debug(f"Generated Fibonacci sequence: {fib_seq[:n]}")
        return fib_seq[:n]
    except Exception as e:
        logger.exception(f"Error in fibonacci_sequence: {e}")
        raise

def complex_root(a, b, c):
    """Calculate and analyze complex roots of a quadratic equation."""
    try:
        logger.info(f"Calculating roots for quadratic equation: {a}x^2 + {b}x + {c} = 0")
        
        if a == 0:
            logger.error("Coefficient 'a' cannot be zero in a quadratic equation")
            raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation")
        
        discriminant = b**2 - 4*a*c
        logger.debug(f"Discriminant calculated: {discriminant}")
        
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            root_type = "real_distinct"
            logger.info(f"Two distinct real roots found: {root1}, {root2}")
        elif discriminant == 0:
            root1 = root2 = -b / (2*a)
            root_type = "real_repeated"
            logger.info(f"One repeated real root found: {root1}")
        else:
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
    except Exception as e:
        logger.exception(f"Error in complex_root: {e}")
        raise