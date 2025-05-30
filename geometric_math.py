import math

def circle_area(radius):
    """Calculate the area of a circle."""
    try:
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        area = math.pi * radius**2
        return area
    except Exception as e:
        raise

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    try:
        if base < 0 or height < 0:
            raise ValueError("Base and height must be non-negative")
        area = 0.5 * base * height
        return area
    except Exception as e:
        raise

def sphere_volume(radius):
    """Calculate the volume of a sphere."""
    try:
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        volume = (4/3) * math.pi * radius**3
        return volume
    except Exception as e:
        raise

def point_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    try:
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance
    except Exception as e:
        raise