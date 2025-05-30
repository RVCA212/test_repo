import math
import cmath

def factorial_recursive(n):
    """Calculate factorial using recursion."""
    try:
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        result = 1 if n <= 1 else n * factorial_recursive(n-1)
        return result
    except Exception as e:
        raise

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms."""
    try:
        fib_seq = [0, 1]
        while len(fib_seq) < n:
            fib_seq.append(fib_seq[-1] + fib_seq[-2])
        return fib_seq[:n]
    except Exception as e:
        raise

def complex_root(a, b, c):
    """Calculate and analyze complex roots of a quadratic equation."""
    try:
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be zero in a quadratic equation")
        
        discriminant = b**2 - 4*a*c
        
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
        return result
    except Exception as e:
        raise