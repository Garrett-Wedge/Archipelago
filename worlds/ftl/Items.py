import typing

from BaseClasses import ItemClassification, Item


class FTLItem(Item):
    game = "FTL"

    def __init__(self, name, player: int = None):
        item_data = item_table[name]
        super(FTLItem, self).__init__(
            name,
            ItemClassification.progression if item_data.progression else ItemClassification.filler,
            item_data.code, player
        )
class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    progression: bool = False
    event: bool = False

# List of FTL Weapons (Vanilla and Advanced Edition)
weapons: typing.Dict[str, ItemData] = {
    "Basic Laser": ItemData(1, False, False),
    "Burst Laser I": ItemData(2, False, False),
    "Burst Laser II": ItemData(3, False, False),
    "Burst Laser III": ItemData(4, False, False),
    "Dual Lasers": ItemData(5, False, False),
    "Heavy Laser I": ItemData(6, False, False),
    "Heavy Laser II": ItemData(7, False, False),
    "Mini Beam": ItemData(8, False, False),
    "Halberd Beam": ItemData(9, False, False),
    "Glaive Beam": ItemData(10, False, False),
    "Ion Blast": ItemData(11, False, False),
    "Ion Blast II": ItemData(12, False, False),
    "Heavy Ion": ItemData(13, False, False),
    "Ion Bomb": ItemData(14, False, False),
    "Small Bomb": ItemData(15, False, False),
    "Breach Bomb I": ItemData(16, False, False),
    "Breach Bomb II": ItemData(17, False, False),
    "Fire Bomb": ItemData(18, False, False),
    "Heal Bomb": ItemData(19, False, False),
    "Pegasus Missile": ItemData(20, False, False),
    "Artemis Missile": ItemData(21, False, False),
    "Hermes Missile": ItemData(22, False, False),
    "Leto Missile": ItemData(23, False, False),
    "Hull Missile": ItemData(24, False, False),
    "Hull Smasher Laser I": ItemData(25, False, False),
    "Hull Smasher Laser II": ItemData(26, False, False),
    "Swarm Missile": ItemData(27, False, False),
    # Advanced Edition Weapons
    "Charge Laser I": ItemData(28, False, False),
    "Charge Laser II": ItemData(29, False, False),
    "Charge Ion": ItemData(30, False, False),
    "Chain Laser": ItemData(31, False, False),
    "Chain Vulcan": ItemData(32, False, False),
    "Ion Stunner": ItemData(33, False, False),
    "Advanced Flak Gun I": ItemData(34, False, False),
    "Flak Gun I": ItemData(35, False, False),
    "Flak Gun II": ItemData(36, False, False),
    "Heavy Crystal I": ItemData(37, False, False),
    "Heavy Crystal II": ItemData(38, False, False),
    "Crystal Burst I": ItemData(39, False, False),
    "Crystal Burst II": ItemData(40, False, False),
    # Add more weapons if needed...
}

# List of FTL Drones (Vanilla and Advanced Edition)
drones: typing.Dict[str, ItemData] = {
    "Anti-Ship Drone I": ItemData(41, False, False),
    "Anti-Ship Drone II": ItemData(42, False, False),
    "Beam Drone I": ItemData(43, False, False),
    "Beam Drone II": ItemData(44, False, False),
    "Combat Drone I": ItemData(45, False, False),
    "Combat Drone II": ItemData(46, False, False),
    "Defense Drone I": ItemData(47, False, False),
    "Defense Drone II": ItemData(48, False, False),
    "Fire Drone": ItemData(49, False, False),
    "Hull Repair Drone": ItemData(50, False, False),
    "Ion Intruder Drone": ItemData(51, False, False),
    "System Repair Drone": ItemData(52, False, False),
    # Advanced Edition Drones
    "Shield Overcharger Drone": ItemData(53, False, False),
    "Anti-Drone Drone": ItemData(54, False, False),
    "Boarding Drone": ItemData(55, False, False),
    # Add more drones if needed...
}

# List of FTL Augmentations (Vanilla and Advanced Edition)
augmentations: typing.Dict[str, ItemData] = {
    "Advanced FTL Navigation": ItemData(56, False, False),
    "Backup DNA Bank": ItemData(57, False, False),
    "Battery Charger": ItemData(58, False, False),
    "Drone Reactor Booster": ItemData(59, False, False),
    "FTL Recharge Booster": ItemData(60, False, False),
    "Hacking Stun": ItemData(61, False, False),
    "Long-Range Scanners": ItemData(62, False, False),
    "Shield Charge Booster": ItemData(63, False, False),
    "Stealth Weapons": ItemData(64, False, False),
    "Titanium System Casing": ItemData(65, False, False),
    "Weapon Pre-Igniter": ItemData(66, False, False),
    # Advanced Edition Augmentations
    "Reconstructive Teleport": ItemData(67, False, False),
    "Explosive Replicator": ItemData(68, False, False),
    "Emergency Respirators": ItemData(69, False, False),
    "Lifeform Scanner": ItemData(70, False, False),
    "Distraction Buoys": ItemData(71, False, False),
    "Reverse Ion Field": ItemData(72, False, False),
    "Crystal Vengeance": ItemData(73, False, False),
    "Zoltan Shield Bypass": ItemData(74, False, False),
    # Add more augmentations if needed...
}

# Combined item table for easier lookup
item_table = {item.code: item for category in (weapons, drones, augmentations) for item in category.values()}