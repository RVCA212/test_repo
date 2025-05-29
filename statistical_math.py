import math

def coefficient_of_variation(data):
    """
    Calculate the coefficient of variation (CV) for a given dataset.
    
    CV is a standardized measure of dispersion of a probability distribution.
    It is defined as the ratio of the standard deviation to the mean.
    
    :param data: List of numerical values
    :return: Coefficient of variation as a percentage
    """
    if not data:
        raise ValueError("Dataset cannot be empty")
    
    mean = sum(data) / len(data)
    variance = sum((x - mean) ** 2 for x in data) / len(data)
    std_dev = math.sqrt(variance)
    
    return (std_dev / mean) * 100 if mean != 0 else float('inf')