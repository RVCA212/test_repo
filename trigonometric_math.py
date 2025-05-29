import math
import logging
import os

# Configure logging
log_dir = 'logs'
os.makedirs(log_dir, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(log_dir, 'trigonometric_math.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

def haversine_distance(lat1, lon1, lat2, lon2):
    """Calculate the great-circle distance between two points on a sphere."""
    try:
        logger.info(f'Calculating haversine distance: ({lat1}, {lon1}) to ({lat2}, {lon2})')
        
        R = 6371  # Earth's radius in kilometers
        
        # Convert latitude and longitude to radians
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        
        # Haversine formula
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
        c = 2 * math.asin(math.sqrt(a))
        
        distance = R * c
        logger.debug(f'Haversine distance calculation result: {distance} km')
        return distance
    except Exception as e:
        logger.exception(f"Error in haversine_distance calculation: {e}")
        raise