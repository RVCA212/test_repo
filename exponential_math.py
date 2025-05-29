import math
import logging
import os

# Configure logging
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'exponential_math.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def power(base, exponent):
    """Calculate base raised to the power of exponent."""
    try:
        logger.info(f'Calculating {base} raised to the power of {exponent}')
        result = math.pow(base, exponent)
        logger.debug(f'Power calculation result: {result}')
        return result
    except Exception as e:
        logger.exception(f"Error in power calculation: {e}")
        raise

def exponential(x):
    """Calculate exponential function (e^x)."""
    try:
        logger.info(f'Calculating exponential of {x}')
        result = math.exp(x)
        logger.debug(f'Exponential calculation result: {result}')
        return result
    except Exception as e:
        logger.exception(f"Error in exponential calculation: {e}")
        raise

def logarithm(x, base=math.e):
    """Calculate logarithm of x with optional base."""
    try:
        logger.info(f'Calculating logarithm of {x} with base {base}')
        if x <= 0:
            logger.error(f'Invalid logarithm input: {x}')
            raise ValueError("Logarithm is only defined for positive numbers")
        result = math.log(x, base)
        logger.debug(f'Logarithm calculation result: {result}')
        return result
    except Exception as e:
        logger.exception(f"Error in logarithm calculation: {e}")
        raise