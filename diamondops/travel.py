
from haversine import haversine

def travel_miles(hotel, field):
    return round(
        haversine(
            (hotel.lat, hotel.lng),
            (field.lat, field.lng)
        ),
        2
    )
