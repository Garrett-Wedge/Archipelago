from typing import Dict, List

from BaseClasses import MultiWorld, Region, Entrance, Item
from worlds.AutoWorld import World
from .Items import item_table, FTLItem
from .Locations import FTLLocationData, location_data_table, FTLLocation
from .Options import ftl_options
from .Regions import create_regions
from .Rules import set_rules


class FTLWorld(World):
    game = "FTL"
    option_definitions = ftl_options

    required_client_version = (0, 5, 0)
    topology_present = False

    item_name_to_id = {item.name: item.code for item in item_table.values()}
    location_name_to_id = {location.region: code for code, location in location_data_table.items()}

    def create_item(self, name: str) -> Item:
        return FTLItem(name, self.player)

    def create_location(self, location_name: str):
        loc_data = location_data_table[location_name]
        return self.create_location_class(location_name, loc_data)

    def create_items(self) -> None:
        item_pool: List[Item] = []
        for name, item in item_table.items():
            if item.code and item.can_create(self.multiworld, self.player):
                item_pool.append(self.create_item(name))

        self.multiworld.itempool += item_pool

    def create_regions(self):
        create_regions(self.multiworld, self.player)

    def set_rules(self):
        set_rules(self.multiworld, self.player)


def create_region(world: MultiWorld, player: int, name: str, locations=None, exits=None):
    ret = Region(name, player, world)
    if locations:
        for location in locations:
            loc_id = location_data_table.get(location, 0)
            location = FTLLocation(player, location, loc_id, ret)
            ret.locations.append(location)
    if exits:
        for exit in exits:
            ret.exits.append(Entrance(player, exit, ret))

    return ret
