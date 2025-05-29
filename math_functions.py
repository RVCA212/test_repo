def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def square(x):
    return x * x

def cube(x):
    return x * x * x

# Test the functions
if __name__ == "__main__":
    add(2, 3)
    subtract(5, 2)
    multiply(4, 6)
    divide(10, 2)
    square(7)
    cube(3)