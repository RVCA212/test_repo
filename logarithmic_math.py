import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def change_of_base(x, base_from, base_to):
    logging.info(f'Converting base for {x} from {base_from} to {base_to}')
    """
    Convert a number from one logarithmic base to another.
    
    :param x: The number to convert
    :param base_from: The original base of the logarithm
    :param base_to: The target base for conversion
    :return: The value of x in the new base
    """
    if x <= 0 or base_from <= 0 or base_to <= 0:
        logging.error(f'Invalid arguments: x={x}, base_from={base_from}, base_to={base_to}')
        raise ValueError("Arguments must be positive")
    
    # Use change of base formula: log_b(x) = log_a(x) / log_a(b)
    result = math.log(x, base_from) / math.log(base_to, base_from)
    logging.info(f'Base conversion result: {result}')
    return result