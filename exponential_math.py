import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

import math

def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    try:
        logger.info(f"Calculating {base} raised to the power of {exponent}")
        result = math.pow(base, exponent)
        logger.info(f"Result of {base}^{exponent}: {result}")
        return result
    except Exception as e:
        logger.exception(f"Error calculating power: {e}")
        raise

def exponential(x):
    """Calculate exponential function (e^x)."""
    try:
        logger.info(f"Calculating exponential of {x}")
        result = math.exp(x)
        logger.info(f"e^{x} = {result}")
        return result
    except Exception as e:
        logger.exception(f"Error calculating exponential: {e}")
        raise

def logarithm(x, base=math.e):
    """Calculate logarithm of x with optional base."""
    try:
        logger.info(f"Calculating logarithm of {x} with base {base}")
        if x <= 0:
            logger.error(f"Invalid input: Logarithm is only defined for positive numbers, got {x}")
            raise ValueError("Logarithm is only defined for positive numbers")
        result = math.log(x, base)
        logger.info(f"log_{base}({x}) = {result}")
        return result
    except Exception as e:
        logger.exception(f"Error calculating logarithm: {e}")
        raise