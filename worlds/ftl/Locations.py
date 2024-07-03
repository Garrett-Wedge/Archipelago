# Locations.py

from typing import NamedTuple, Callable, Optional, Dict

from BaseClasses import Location


class FTLLocation(Location):
    game = "FTL"

class FTLLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[[int], bool] = lambda player: True

location_data_table: Dict[str, FTLLocationData] = {
    "First Fight": FTLLocationData(region="First Fight", address=1),
    "Sector 1 - Location 1": FTLLocationData(region="Sector 1", address=2),
    "Sector 2 - Location 1": FTLLocationData(region="Sector 2", address=3),
    # Add more locations as needed...
}

def get_location_by_code(code: int) -> Optional[FTLLocationData]:
    for loc in location_data_table.values():
        if loc.address == code:
            return loc
    return None

def get_location_by_name(name: str) -> Optional[FTLLocationData]:
    return location_data_table.get(name, None)