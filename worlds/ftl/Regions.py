def create_regions(world, player: int):
    from . import create_region
    from .Locations import location_data_table

    world.regions += [
        create_region(world, player, 'Menu', None, ['Start Game']),
        create_region(world, player, 'Sector 1', [location for location in location_data_table])
    ]

    # link up our region with the entrance we just made
    world.get_entrance('Start Game', player).connect(world.get_region('Sector 1', player))
