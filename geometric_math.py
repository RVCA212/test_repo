import math

def circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius**2

def triangle_area(base, height):
    """Calculate the area of a triangle."""
    return 0.5 * base * height

def sphere_volume(radius):
    """Calculate the volume of a sphere."""
    return (4/3) * math.pi * radius**3

def point_distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)