import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

import math

def change_of_base(x, base_from, base_to):
    """Convert a number from one logarithmic base to another."""
    try:
        logger.info(f"Converting logarithm of {x} from base {base_from} to base {base_to}")
        if x <= 0 or base_from <= 0 or base_to <= 0:
            logger.error(f"Invalid input: All arguments must be positive, got x={x}, base_from={base_from}, base_to={base_to}")
            raise ValueError("Arguments must be positive")
        
        # Use change of base formula: log_b(x) = log_a(x) / log_a(b)
        result = math.log(x, base_from) / math.log(base_to, base_from)
        logger.info(f"log_{base_to}({x}) (calculated via base {base_from}) = {result}")
        return result
    except Exception as e:
        logger.exception(f"Error converting logarithmic base: {e}")
        raise