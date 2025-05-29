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
        logging.FileHandler(os.path.join(log_dir, 'statistical_math.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def coefficient_of_variation(data):
    """Calculate the coefficient of variation (CV) for a given dataset."""
    try:
        logger.info(f'Calculating coefficient of variation for dataset of length {len(data)}')
        
        if not data:
            logger.error('Attempted to calculate CV for empty dataset')
            raise ValueError("Dataset cannot be empty")
        
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std_dev = math.sqrt(variance)
        
        cv = (std_dev / mean) * 100 if mean != 0 else float('inf')
        logger.info(f'Coefficient of variation: {cv}')
        return cv
    except Exception as e:
        logger.exception(f"Error in coefficient_of_variation: {e}")
        raise