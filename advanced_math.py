import math
import cmath
import logging
import numpy as np
from typing import List, Dict, Union, Tuple

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def factorial_recursive(n: int) -> int:
    """Calculate factorial using recursion with memoization and logging."""
    # Memoization cache to improve performance
    _factorial_cache = {}
    
    def _factorial(n: int) -> int:
        if n in _factorial_cache:
            return _factorial_cache[n]
        
        logger.info(f"Calculating factorial for n = {n}")
        if n < 0:
            logger.error(f"Factorial attempted with negative number: {n}")
            raise ValueError("Factorial is not defined for negative numbers")
        
        result = 1 if n <= 1 else n * _factorial(n-1)
        _factorial_cache[n] = result
        logger.info(f"Factorial of {n} is {result}")
        return result
    
    return _factorial(n)

def fibonacci_generator(n: int) -> List[int]:
    """
    Generate Fibonacci sequence with advanced properties.
    
    Includes golden ratio approximation and checks for interesting mathematical properties.
    """
    logger.info(f"Generating Fibonacci sequence for {n} terms")
    
    # Using generator for memory efficiency
    def fib_gen():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    sequence = list(next(fib_gen()) for _ in range(n))
    
    # Calculate golden ratio approximation
    golden_ratio_approx = sequence[-1] / sequence[-2] if n > 1 else None
    
    logger.debug(f"Generated Fibonacci sequence: {sequence}")
    logger.info(f"Golden Ratio Approximation: {golden_ratio_approx}")
    
    return {
        "sequence": sequence,
        "golden_ratio_approx": golden_ratio_approx,
        "is_perfect_sequence": all(x % 2 == (0 if i % 2 == 0 else 1) for i, x in enumerate(sequence))
    }

def complex_root_analysis(a: float, b: float, c: float) -> Dict[str, Union[Tuple, str, float]]:
    """
    Advanced complex root analysis with additional mathematical insights.
    
    Provides deeper mathematical context about the roots and equation.
    """
    logger.info(f"Analyzing roots for equation: {a}x^2 + {b}x + {c} = 0")
    
    if a == 0:
        logger.error("Coefficient 'a' cannot be zero in a quadratic equation")
        raise ValueError("Not a valid quadratic equation")
    
    # Advanced root computation using numpy for precision
    discriminant = b**2 - 4*a*c
    roots = np.roots([a, b, c])
    
    # Categorize roots with more nuanced classification
    def classify_roots(roots, discriminant):
        if discriminant > 0:
            return "rational_real_distinct"
        elif discriminant == 0:
            return "rational_real_repeated"
        else:
            return "irrational_complex_conjugate"
    
    root_classification = classify_roots(roots, discriminant)
    
    result = {
        "roots": tuple(roots),
        "type": root_classification,
        "sum_of_roots": sum(roots),
        "product_of_roots": np.prod(roots),
        "discriminant": discriminant,
        "equation": f"{a}x^2 + {b}x + {c} = 0",
        "root_symmetry": all(abs(root.imag) < 1e-10 for root in roots)
    }
    
    logger.debug(f"Comprehensive root analysis: {result}")
    return result

def prime_sequence_generator(limit: int = 100) -> Dict[str, Union[List[int], float]]:
    """
    Generate prime numbers with advanced mathematical analysis.
    
    Includes density calculation and distribution insights.
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True
    
    primes = [num for num in range(2, limit) if is_prime(num)]
    
    # Advanced prime number insights
    analysis = {
        "sequence": primes,
        "count": len(primes),
        "density": len(primes) / limit,
        "twin_primes": [(p, p+2) for p in primes if is_prime(p+2)],
        "largest_prime": max(primes) if primes else None
    }
    
    return analysis