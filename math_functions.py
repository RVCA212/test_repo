import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def add(a, b):
    logging.info(f'Adding {a} and {b}')
    return a + b

def subtract(a, b):
    logging.info(f'Subtracting {b} from {a}')
    return a - b

def multiply(a, b):
    logging.info(f'Multiplying {a} and {b}')
    return a * b

def divide(a, b):
    logging.info(f'Dividing {a} by {b}')
    if b == 0:
        logging.error('Attempted division by zero')
        raise ValueError("Cannot divide by zero")
    return a / b

def square(x):
    logging.info(f'Squaring {x}')
    return x * x

def cube(x):
    logging.info(f'Cubing {x}')
    return x * x * x

# Test the functions
if __name__ == "__main__":
    print("Testing math functions:")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"5 - 2 = {subtract(5, 2)}")
    print(f"4 * 6 = {multiply(4, 6)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"7² = {square(7)}")
    print(f"3³ = {cube(3)}")