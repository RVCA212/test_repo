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
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def square(x):
    """Calculate the square of a number."""
    return x * x

def cube(x):
    """Calculate the cube of a number."""
    return x * x * x

# Test the functions
if __name__ == "__main__":
    add(2, 3)
    subtract(5, 2)
    multiply(4, 6)
    divide(10, 2)
    square(7)
    cube(3)