import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    logger.info(f'Calculating {base} raised to the power of {exponent}')
    result = math.pow(base, exponent)
    logger.debug(f'Power calculation result: {result}')
    return result

def exponential(x):
    """Calculate exponential function (e^x)."""
    logger.info(f'Calculating exponential of {x}')
    result = math.exp(x)
    logger.debug(f'Exponential calculation result: {result}')
    return result

def logarithm(x, base=math.e):
    """Calculate logarithm of x with optional base."""
    logger.info(f'Calculating logarithm of {x} with base {base}')
    result = math.log(x, base)
    logger.debug(f'Logarithm calculation result: {result}')
    return result