import math

def generate_fibonacci_spiral(iterations=5):
    """
    Generate coordinates for a Fibonacci spiral.
    
    Args:
        iterations (int): Number of spiral iterations to generate
    
    Returns:
        list: List of (x, y) coordinates tracing a Fibonacci spiral
    """
    spiral_coords = []
    a, b = 0, 1
    angle = 0
    
    for _ in range(iterations):
        # Calculate new Fibonacci number
        c = a + b
        
        # Convert polar to Cartesian coordinates
        x = c * math.cos(angle)
        y = c * math.sin(angle)
        
        spiral_coords.append((x, y))
        
        # Update Fibonacci sequence and angle
        a, b = b, c
        angle += math.pi / 2  # 90-degree rotation
    
    return spiral_coords

# Example usage
if __name__ == "__main__":
    print(generate_fibonacci_spiral())