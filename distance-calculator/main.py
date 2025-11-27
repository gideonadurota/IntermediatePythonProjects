from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from dataclasses import dataclass
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

# geolocator = Nominatim(user_agent='distance-calculator')
# location = geolocator.geocode('Lekki Phase One, Lagos, Nigeria')
# print(location.latitude, location.longitude)
# location = geolocator.geocode('Lekki Phase One, Lagos, Nigeria')
# print(location.address)
@dataclass
class Coordinates:
    latitude: float
    longitude: float

    def coordinates(self):
        return self.latitude, self.longitude

def get_coordinates(address: str) -> Coordinates | None:
    geolocator = Nominatim(user_agent='distance-calculator', timeout=5) # add timeout because of timeout error
    try:
        location = geolocator.geocode(address)
        if location:
            return Coordinates(latitude=location.latitude, longitude=location.longitude)
        else:
            print(f"Could not find coordinates for address: {address}")
            return None
    except GeocoderTimedOut:
        print(f"Geocoding service timed out for address: {address}")
        return None
    except GeocoderServiceError as e:
        print(f"Geocoding service error: {e}")
        return None

def calculate_distance_km(home: Coordinates, target: Coordinates) -> float | None:
    if home and target:
        distance = geodesic(home.coordinates(), target.coordinates()).km
        return distance

def get_distance(home_address: str, target_address: str) -> float | None:
    home_coordinates = get_coordinates(home_address)
    target_coordinates = get_coordinates(target_address)

    if distance := calculate_distance_km(home_coordinates, target_coordinates):
        print(f'{home_address} -> {distance:.2f}')
        print(f'distance = {distance:.2f} km')
        return distance

def main():
    home_address: str = input('Home address: ')
    target_address: str = input('Target address: ')
    print("Calculating...")
    get_distance(home_address, target_address)

if __name__ == '__main__':
    main()