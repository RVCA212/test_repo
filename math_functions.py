import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

def add(a, b):
    """Add two numbers."""
    logger.info(f"Adding {a} and {b}")
    result = a + b
    logger.info(f"{a} + {b} = {result}")
    return result

def subtract(a, b):
    """Subtract b from a."""
    logger.info(f"Subtracting {b} from {a}")
    result = a - b
    logger.info(f"{a} - {b} = {result}")
    return result

def multiply(a, b):
    """Multiply two numbers."""
    logger.info(f"Multiplying {a} and {b}")
    result = a * b
    logger.info(f"{a} * {b} = {result}")
    return result

def divide(a, b):
    """Divide a by b."""
    logger.info(f"Dividing {a} by {b}")
    if b == 0:
        logger.error("Attempted to divide by zero")
        raise ValueError("Cannot divide by zero")
    result = a / b
    logger.info(f"{a} / {b} = {result}")
    return result

def square(x):
    """Calculate the square of a number."""
    logger.info(f"Calculating square of {x}")
    result = x * x
    logger.info(f"Square of {x} is {result}")
    return result

def cube(x):
    """Calculate the cube of a number."""
    logger.info(f"Calculating cube of {x}")
    result = x * x * x
    logger.info(f"Cube of {x} is {result}")
    return result

# Test the functions
if __name__ == "__main__":
    logger.info("Running math function tests")
    add(2, 3)
    subtract(5, 2)
    multiply(4, 6)
    divide(10, 2)
    square(7)
    cube(3)
    logger.info("Math function tests completed")