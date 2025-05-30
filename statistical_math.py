import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

import math

def coefficient_of_variation(data):
    """Calculate the coefficient of variation (CV) for a given dataset."""
    try:
        logger.info(f"Calculating coefficient of variation for dataset with {len(data)} elements")
        
        if not data:
            logger.error("Empty dataset provided")
            raise ValueError("Dataset cannot be empty")
        
        mean = sum(data) / len(data)
        logger.debug(f"Dataset mean: {mean}")
        
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std_dev = math.sqrt(variance)
        logger.debug(f"Dataset standard deviation: {std_dev}")
        
        cv = (std_dev / mean) * 100 if mean != 0 else float('inf')
        logger.info(f"Coefficient of Variation: {cv}")
        
        return cv
    except Exception as e:
        logger.exception(f"Error calculating coefficient of variation: {e}")
        raise