import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

import math

def circle_area(radius):
    """Calculate the area of a circle."""
    try:
        logger.info(f"Calculating area of circle with radius {radius}")
        if radius < 0:
            logger.error(f"Invalid input: Radius cannot be negative, got {radius}")
            raise ValueError("Radius cannot be negative")
        area = math.pi * radius**2
        logger.info(f"Area of circle with radius {radius}: {area}")
        return area
    except Exception as e:
        logger.exception(f"Error calculating circle area: {e}")
        raise

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    try:
        logger.info(f"Calculating area of triangle with base {base} and height {height}")
        if base < 0 or height < 0:
            logger.error(f"Invalid input: Base and height must be non-negative, got base={base}, height={height}")
            raise ValueError("Base and height must be non-negative")
        area = 0.5 * base * height
        logger.info(f"Area of triangle with base {base} and height {height}: {area}")
        return area
    except Exception as e:
        logger.exception(f"Error calculating triangle area: {e}")
        raise

def sphere_volume(radius):
    """Calculate the volume of a sphere."""
    try:
        logger.info(f"Calculating volume of sphere with radius {radius}")
        if radius < 0:
            logger.error(f"Invalid input: Radius cannot be negative, got {radius}")
            raise ValueError("Radius cannot be negative")
        volume = (4/3) * math.pi * radius**3
        logger.info(f"Volume of sphere with radius {radius}: {volume}")
        return volume
    except Exception as e:
        logger.exception(f"Error calculating sphere volume: {e}")
        raise

def point_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    try:
        logger.info(f"Calculating distance between points ({x1}, {y1}) and ({x2}, {y2})")
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        logger.info(f"Distance between ({x1}, {y1}) and ({x2}, {y2}): {distance}")
        return distance
    except Exception as e:
        logger.exception(f"Error calculating point distance: {e}")
        raise