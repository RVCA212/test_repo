import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

import math

def coefficient_of_variation(data):
    """Calculate the coefficient of variation (CV) for a given dataset."""
    try:
        if not data:
            raise ValueError("Dataset cannot be empty")
        
        mean = sum(data) / len(data)
        variance = sum((x - mean) ** 2 for x in data) / len(data)
        std_dev = math.sqrt(variance)
        
        cv = (std_dev / mean) * 100 if mean != 0 else float('inf')
        return cv
    except Exception as e:
        raise