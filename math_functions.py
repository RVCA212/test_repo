import logging
import os

# Configure logging
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'math_functions.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def add(a, b):
    """Add two numbers."""
    try:
        logger.info(f'Adding {a} and {b}')
        result = a + b
        logger.debug(f'Addition result: {result}')
        return result
    except Exception as e:
        logger.exception(f"Error in addition: {e}")
        raise

def subtract(a, b):
    """Subtract b from a."""
    try:
        logger.info(f'Subtracting {b} from {a}')
        result = a - b
        logger.debug(f'Subtraction result: {result}')
        return result
    except Exception as e:
        logger.exception(f"Error in subtraction: {e}")
        raise

def multiply(a, b):
    """Multiply two numbers."""
    try:
        logger.info(f'Multiplying {a} and {b}')
        result = a * b
        logger.debug(f'Multiplication result: {result}')
        return result
    except Exception as e:
        logger.exception(f"Error in multiplication: {e}")
        raise

def divide(a, b):
    """Divide a by b."""
    try:
        logger.info(f'Dividing {a} by {b}')
        if b == 0:
            logger.error('Attempted division by zero')
            raise ValueError("Cannot divide by zero")
        result = a / b
        logger.debug(f'Division result: {result}')
        return result
    except Exception as e:
        logger.exception(f"Error in division: {e}")
        raise

def square(x):
    """Calculate the square of a number."""
    try:
        logger.info(f'Calculating square of {x}')
        result = x * x
        logger.debug(f'Square calculation result: {result}')
        return result
    except Exception as e:
        logger.exception(f"Error in square calculation: {e}")
        raise

def cube(x):
    """Calculate the cube of a number."""
    try:
        logger.info(f'Calculating cube of {x}')
        result = x * x * x
        logger.debug(f'Cube calculation result: {result}')
        return result
    except Exception as e:
        logger.exception(f"Error in cube calculation: {e}")
        raise

# Test the functions
if __name__ == "__main__":
    add(2, 3)
    subtract(5, 2)
    multiply(4, 6)
    divide(10, 2)
    square(7)
    cube(3)