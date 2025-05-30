import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

import math

def change_of_base(x, base_from, base_to):
    """Convert a number from one logarithmic base to another."""
    try:
        if x <= 0 or base_from <= 0 or base_to <= 0:
            raise ValueError("Arguments must be positive")
        
        # Use change of base formula: log_b(x) = log_a(x) / log_a(b)
        result = math.log(x, base_from) / math.log(base_to, base_from)
        return result
    except Exception as e:
        raise