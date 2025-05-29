import math

def power(base, exponent):
    """
    Calculate base raised to the power of exponent.
    
    Args:
        base (float): The base number
        exponent (float): The exponent
    
    Returns:
        float: base raised to the power of exponent
    """
    return math.pow(base, exponent)

def exponential(x):
    """
    Calculate exponential function (e^x).
    
    Args:
        x (float): The input value
    
    Returns:
        float: e raised to the power of x
    """
    return math.exp(x)

def logarithm(x, base=math.e):
    """
    Calculate logarithm of x with optional base.
    
    Args:
        x (float): The input value
        base (float, optional): The logarithm base. Defaults to e.
    
    Returns:
        float: logarithm of x with given base
    """
    return math.log(x, base)