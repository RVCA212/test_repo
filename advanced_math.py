import math

def factorial_recursive(n):
    """Calculate factorial using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return 1 if n <= 1 else n * factorial_recursive(n-1)

def fibonacci_sequence(n):
    """Generate Fibonacci sequence up to n terms."""
    fib_seq = [0, 1]
    while len(fib_seq) < n:
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

def complex_root(a, b, c):
    """Calculate complex roots of a quadratic equation."""
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        real_part = -b / (2*a)
        imag_part = math.sqrt(abs(discriminant)) / (2*a)
        return (complex(real_part, imag_part), complex(real_part, -imag_part))
    else:
        return None