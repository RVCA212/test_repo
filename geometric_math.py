import math
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def circle_area(radius):
    """Calculate the area of a circle."""
    logger.info(f"Calculating area of circle with radius {radius}")
    if radius < 0:
        logger.error(f"Negative radius provided: {radius}")
        raise ValueError("Radius cannot be negative")
    area = math.pi * radius**2
    logger.debug(f"Circle area calculation result: {area}")
    return area

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    logger.info(f"Calculating area of triangle with base {base} and height {height}")
    if base < 0 or height < 0:
        logger.error(f"Negative base or height: base={base}, height={height}")
        raise ValueError("Base and height must be non-negative")
    area = 0.5 * base * height
    logger.debug(f"Triangle area calculation result: {area}")
    return area

def sphere_volume(radius):
    """Calculate the volume of a sphere."""
    logger.info(f"Calculating volume of sphere with radius {radius}")
    if radius < 0:
        logger.error(f"Negative radius provided: {radius}")
        raise ValueError("Radius cannot be negative")
    volume = (4/3) * math.pi * radius**3
    logger.debug(f"Sphere volume calculation result: {volume}")
    return volume

def point_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    logger.info(f"Calculating distance between points ({x1},{y1}) and ({x2},{y2})")
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    logger.debug(f"Point distance calculation result: {distance}")
    return distance