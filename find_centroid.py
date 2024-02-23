import logging
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut
import time
import sys

# Set up logging
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)

logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)


def retry_on_timeout(func):
    def wrapper(*args, **kwargs):
        retries = 3
        delay = 0.5
        for _ in range(retries):
            try:
                return func(*args, **kwargs)
            except GeocoderTimedOut:
                logger.info("Geocoding service timed out. Retrying...")
                time.sleep(delay)
        raise GeocoderTimedOut("Geocoding service timed out after multiple retries.")
    return wrapper

@retry_on_timeout
def geocode_city(city):
    geolocator = Nominatim(user_agent="city_locator")
    location = geolocator.geocode(city)
    if location:
        return (location.latitude, location.longitude)
    else:
        raise GeocoderTimedOut(f"Could not find coordinates for {city}")

def find_centroid(city_names):
    coordinates = []
    for city in city_names:
        logger.info(f'Finding coordinates of {city}')
        coordinates.append(geocode_city(city))
    centroid = [sum(x) / len(coordinates) for x in zip(*coordinates)]
    return centroid

def find_closest_city_to_centroid(centroid):
    geolocator = Nominatim(user_agent="city_locator")
    closest_city = None
    min_distance = float('inf')
    for location in geolocator.reverse(centroid, exactly_one=False):
        city_coords = (location.latitude, location.longitude)
        distance = geodesic(centroid, city_coords).kilometers
        if distance < min_distance:
            min_distance = distance
            closest_city = location.address
    return closest_city

def main():
    if len(sys.argv) < 2:
        print("Usage: python find_centroid.py city1,city2,city3,...")
        sys.exit(1)
    
    city_names = sys.argv[1].split(',')
    
    centroid = find_centroid(city_names)
    print(f"\n\nCentroid coordinates: \033[92m{centroid}\033[0m")
    
    closest_city = find_closest_city_to_centroid(centroid)
    print(f"\n\nThe closest city to the centroid is: \033[92m{closest_city}\033[0m")

if __name__ == "__main__":
    main()