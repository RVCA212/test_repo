import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def add(a, b):
    logger.info(f'Adding {a} and {b}')
    result = a + b
    logger.debug(f'Addition result: {result}')
    return result

def subtract(a, b):
    logger.info(f'Subtracting {b} from {a}')
    result = a - b
    logger.debug(f'Subtraction result: {result}')
    return result

def multiply(a, b):
    logger.info(f'Multiplying {a} and {b}')
    result = a * b
    logger.debug(f'Multiplication result: {result}')
    return result

def divide(a, b):
    logger.info(f'Dividing {a} by {b}')
    if b == 0:
        logger.error('Attempted division by zero')
        raise ValueError("Cannot divide by zero")
    result = a / b
    logger.debug(f'Division result: {result}')
    return result

def square(x):
    logger.info(f'Calculating square of {x}')
    result = x * x
    logger.debug(f'Square calculation result: {result}')
    return result

def cube(x):
    logger.info(f'Calculating cube of {x}')
    result = x * x * x
    logger.debug(f'Cube calculation result: {result}')\n    return result

# Test the functions
if __name__ == "__main__":
    add(2, 3)
    subtract(5, 2)
    multiply(4, 6)
    divide(10, 2)
    square(7)
    cube(3)