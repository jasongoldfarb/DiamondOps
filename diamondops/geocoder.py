
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent='diamondops')

def geocode_address(address):
    location = geolocator.geocode(address)
    if not location:
        raise ValueError(f'Unable to geocode: {address}')
    return location.latitude, location.longitude
