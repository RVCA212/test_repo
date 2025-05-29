import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def coefficient_of_variation(data):
    logging.info(f'Calculating coefficient of variation for dataset of length {len(data)}')
    """
    Calculate the coefficient of variation (CV) for a given dataset.
    
    CV is a standardized measure of dispersion of a probability distribution.
    It is defined as the ratio of the standard deviation to the mean.
    
    :param data: List of numerical values
    :return: Coefficient of variation as a percentage
    """
    if not data:
        logging.error('Attempted to calculate CV for empty dataset')
        raise ValueError("Dataset cannot be empty")
    
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    
    cv = (std_dev / mean) * 100 if mean != 0 else float('inf')
    logging.info(f'Coefficient of variation: {cv}')
    return cv