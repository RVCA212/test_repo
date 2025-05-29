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
        logging.FileHandler(os.path.join(log_dir, 'logarithmic_math.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def change_of_base(x, base_from, base_to):
    """Convert a number from one logarithmic base to another."""
    try:
        logger.info(f'Converting base for {x} from {base_from} to {base_to}')
        
        if x <= 0 or base_from <= 0 or base_to <= 0:
            logger.error(f'Invalid arguments: x={x}, base_from={base_from}, base_to={base_to}')
            raise ValueError("Arguments must be positive")
        
        # Use change of base formula: log_b(x) = log_a(x) / log_a(b)
        result = math.log(x, base_from) / math.log(base_to, base_from)
        logger.info(f'Base conversion result: {result}')
        return result
    except Exception as e:
        logger.exception(f"Error in change_of_base: {e}")
        raise