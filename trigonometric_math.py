import logging

# Configure logging for this module
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

import math

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two points on a sphere."""
    try:
        logger.info(f"Calculating Haversine distance between points: ({lat1}, {lon1}) and ({lat2}, {lon2})")
        
        R = 6371  # Earth's radius in kilometers
        logger.debug(f"Using Earth radius: {R} km")
        
        # Convert latitude and longitude to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        logger.debug(f"Converted points to radians: ({lat1}, {lon1}) and ({lat2}, {lon2})")
        
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        distance = R * c
        logger.info(f"Haversine distance: {distance} km")
        
        return distance
    except Exception as e:
        logger.exception(f"Error calculating Haversine distance: {e}")
        raise