import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

import math

def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    try:
        result = math.pow(base, exponent)
        return result
    except Exception as e:
        raise

def exponential(x):
    """Calculate exponential function (e^x)."""
    try:
        result = math.exp(x)
        return result
    except Exception as e:
        raise

def logarithm(x, base=math.e):
    """Calculate logarithm of x with optional base."""
    try:
        if x <= 0:
            raise ValueError("Logarithm is only defined for positive numbers")
        result = math.log(x, base)
        return result
    except Exception as e:
        raise