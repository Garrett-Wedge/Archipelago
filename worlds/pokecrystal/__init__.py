from typing import NamedTuple, Union
import logging

from .Options import pokemon_crystal_options
from .Items import *

from ..AutoWorld import World


class PokemonCrystalWorld(World):
    """
    Pokemon Crystal is a role-playing game released in 2000. It is an early part of a very popular, long-running
    franchise. This game features turn-based combat between Pokemon trainers. You play as a character who collects
    Pokemon who help you navigate the Johto and Kanto regions, with the goal of defeating the elite four and becoming
    the champion.
    """
    game = "Pokemon Crystal"
    options = pokemon_crystal_options
    topology_present = False
    item_name_to_id = {item_name: pc_data_to_ap_id(data, False) for item_name, data in item_table}
    # TODO: implement
    location_name_to_id = {
        "Cheat Console": -1,
        "Server": -2
    }
    hidden = True

    def create_item(self, name: str) -> Item:
        if name == "Nothing":
            return Item(name, False, -1, self.player)
        raise KeyError(name)


class PlandoItem(NamedTuple):
    item: str
    location: str
    world: Union[bool, str] = False  # False -> own world, True -> not own world
    from_pool: bool = True  # if item should be removed from item pool
    force: str = 'silent'  # false -> warns if item not successfully placed. true -> errors out on failure to place item.

    def warn(self, warning: str):
        if self.force in ['true', 'fail', 'failure', 'none', 'false', 'warn', 'warning']:
            logging.warning(f'{warning}')
        else:
            logging.debug(f'{warning}')

    def failed(self, warning: str, exception=Exception):
        if self.force in ['true', 'fail', 'failure']:
            raise exception(warning)
        else:
            self.warn(warning)


class PlandoConnection(NamedTuple):
    entrance: str
    exit: str
    direction: str  # entrance, exit or both
