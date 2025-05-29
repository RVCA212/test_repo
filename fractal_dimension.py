import math

def box_counting_dimension(points, min_box_size=1, max_box_size=None):
    """
    Calculate the fractal dimension of a set of points using box-counting method.
    
    Args:
        points (list): List of (x, y) coordinate tuples
        min_box_size (float): Smallest box size to start with
        max_box_size (float): Largest box size to consider
    
    Returns:
        float: Estimated fractal dimension
    """
    # If max_box_size not provided, calculate based on point spread
    if max_box_size is None:
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        max_box_size = max(max(x_coords) - min(x_coords), 
                           max(y_coords) - min(y_coords))
    
    # Track number of boxes needed at different scales
    box_counts = []
    box_sizes = []
    
    current_box_size = max_box_size
    while current_box_size >= min_box_size:
        # Create a grid of boxes
        covered_boxes = set()
        for x, y in points:
            box_x = math.floor(x / current_box_size)
            box_y = math.floor(y / current_box_size)
            covered_boxes.add((box_x, box_y))
        
        box_counts.append(len(covered_boxes))
        box_sizes.append(current_box_size)
        
        # Reduce box size by half
        current_box_size /= 2
    
    # Linear regression to calculate fractal dimension
    if len(box_sizes) > 1:
        log_box_sizes = [math.log(size) for size in box_sizes]
        log_box_counts = [math.log(count) for count in box_counts]
        
        # Compute slope
        n = len(log_box_sizes)
        sum_x = sum(log_box_sizes)
        sum_y = sum(log_box_counts)
        sum_xy = sum(x*y for x, y in zip(log_box_sizes, log_box_counts))
        sum_x_squared = sum(x*x for x in log_box_sizes)
        
        slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x * sum_x)
        
        return -slope  # Negative slope gives fractal dimension
    
    return 0

# Example usage
if __name__ == "__main__":
    # Example point cloud (could represent a fractal-like shape)
    points = [(x, math.sin(x) * math.cos(x)) for x in range(100)]
    print(f"Fractal Dimension: {box_counting_dimension(points)}")