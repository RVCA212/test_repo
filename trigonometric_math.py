import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two points on a sphere."""
    try:
        R = 6371  # Earth's radius in kilometers
        
        # Convert latitude and longitude to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        distance = R * c
        return distance
    except Exception as e:
        raise