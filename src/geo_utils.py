import pandas as pd
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
from haversine import haversine, Unit


# geolocator for location data fill
geolocator = Nominatim(user_agent="Ivan")
# rate limit to prevent block
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

def fill_missing_location(
        address: str|None,
        city: str|None,
        state: str|None,
        postal_code: str|None
) -> dict[str, str|None]:
    if address:
        available_data = [el for el in [address, city, state, postal_code] if el]
        location = geocode(",".join(available_data)).raw['display_name'].split(",")
        return  {
            "street_address": address.lower(),
            "city": location[-5].strip().lower(),
            "state": location[-3].strip().lower(),
            "postal_code": location[-2].strip().lower()
        }
    else:
        return {
            "street_address": address,
            "city": city,
            "state": state,
            "postal_code": postal_code
        }


def fill_missing_location_row(row: pd.Series) -> pd.Series:
    try:
        address = row["street_address"]
        city = row["city"]
        state = row["state"]
        postal_code = row["postal_code"]
        if not all([address, city, state, postal_code]):
            location = fill_missing_location(address=address, city=city, state=state, postal_code=postal_code)
            output = row.copy()
            output.update(location)
            return output
        else:
            return row
    except:
        return row


def find_coordinates(address: str, city: str, state: str, postal_code: str) -> tuple[float, float]|None:
    location = geocode(",".join([address, city, state, postal_code]))
    if location:
        return location.latitude, location.longitude
    else:
        return None


def calculate_distance(loc1: tuple[float, float], loc2: tuple[float, float]) -> float|None:
    if loc1 and loc2:
        return haversine(loc1, loc2, unit=Unit.KILOMETERS)
