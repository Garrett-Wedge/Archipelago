import typing

from jinja2.sandbox import unsafe

from Options import Option, Toggle, Choice


class RandomizerMode(Choice):
    """Sets the mode of randomization to use."""
    # TODO: add more details about each mode
    displayname = "Randomizer Mode"
    option_classic_key_item_rando = 0
    option_crazy = 1
    option_crazy_with_hidden_items = 2
    option_easy = 3
    option_easy_key_item_rando = 4
    option_extreme = 5
    option_extreme_14_badge = 6
    option_extreme_johto_mode = 7
    option_extreme_key_item_rando = 8
    option_extreme_with_hidden_items = 9
    option_johto_mode = 10
    option_less_extreme = 11
    option_maximum = 12
    option_maximum_with_hints = 13
    option_nightmare = 14
    option_nightmare_with_hidden_items = 15
    option_old_standard = 16
    option_standard = 17
    option_tm_plus_key_items = 18
    option_tricky = 19
    option_tricky_key_item_rando = 20
    option_vintage = 21
    default = 17


class AllMonItemsAvailable(Toggle):
    """Ensures that all items which boost the power of a specific pokemon (Stick, Metal Powder, Lucky Punch, Light Ball,
     Thick Club) are in the item pool."""
    displayname = "All Pokemon boosting items available"


class AllTMsAvailable(Toggle):
    """Ensures that all 50 TMs are available. TMs that appear multiple times in the vanilla game will still have
    multiple copies. TMs that normally appear in shops will not have additional copies added to the item pool (other
    than those that already exist). All game corner TMs are added to the item pool, as they are way too expensive and
    slow to get normally. Note that this is relative to the checks available under your current settings, thus TM03 for
    example might be both in the item pool and also available at night in Celadon. """
    displayname = "All TMs available"


class AllTypeBoostersAvailable(Toggle):
    """Ensures that all items which boost the power of a certain type's moves are present in the item pool. """
    displayname = "All type boosting items available"


class BanAnnoyingLocations(Toggle):
    """Prevents items needed to defeat red from being located in the following locations, Ho-Oh chamber, Route 4, Tin
    Tower Rainbow Wing Gift, Elm's SS Ticket, Dragon's Den and Solarbeam TM. Note that this setting does not affect
    Clair's badge. Note that non-progress items can still be placed in this location while this setting is enabled."""
    displayname = "No Annoying Location"


class BanMildlyInconvenientLocations(Toggle):
    """Prevents items needed to defeat red from being located in the following locations, Ho-Oh chamber, Route 4, Tin
    Tower Rainbow Wing Gift, Elm's SS Ticket, Dragon's Den, Solarbeam TM, False Director, Items on Route 25, Left side
    of Tohjo Falls Items, Mystery Egg Gift, Masterball Gift, Secretpotion Gift and Soft Sand. Note that this setting
    does not affect Clair's badge. Note that non-progress items can still be placed in this location while this setting
    is enabled."""
    displayname = "No Mildly Inconvenient Location"


class BanNastyLocations(Toggle):
    """Prevents items needed to defeat red from being located in the following locations, Ho-Oh chamber, Route 4, Tin
    Tower Rainbow Wing Gift and Elm's SS Ticket. Note that non-progress items can still be placed in this location while
     this setting is enabled."""
    displayname = "No Nasty Location"


class BerryTrees(Toggle):
    """Adds berry tree items to the randomization."""
    displayname = "Berry Trees"


class BugCatchingContest(Toggle):
    """Includes the prizes for completing the bug catching contest (all four items) into the item pool. The bug catching
     contest will be able to entered everyday and as many times as you desire."""
    displayname = "Bug Catching Contest"


class CardRandomization(Toggle):
    """Makes logic aware that Pokegear and Pokegear Cards are being randomized. Also shuffles the Pokedex."""
    displayname = "Randomize Pokegear and Pokegear Cards"


class CardRandomizationButNotDex(Toggle):
    """Makes logic aware that Pokegear and Pokegear Cards are being randomized. Does not shuffle the Pokedex."""
    displayname = "Randomize Pokegear and Pokegear Cards but Not the Pokedex"


class DefinitelyNoEarlySabrina(Toggle):
    """Prevents Sabrina being required before you can access 7 other gyms"""
    displayname = "Definitely no early Sabrina"


class DeleteFly(Toggle):
    """Makes HM02 (Fly) become HM02 (Splash). While both Fly and Splash are moves which cause a temporary increase in
    altitude, Splash is perhaps a bit less useful than Fly is. I don't understand why you want to do this, but OK."""
    displayname = "Delete Fly"


class DontReplaceGoodItems(Toggle):
    """Ensures that when adding items to the pool, the following never gets replaced. TMs, Hyper Potions, Max Revives,
    Full Restores, Max Potions, Max Elixers and Masterballs"""
    displayname = "Don't replace good items"


class EnableTinTower(Toggle):
    """Changes Tin Tower to item rando access rules. As in vanilla, Suicune can be fought if you have the clear bell
    and beat Morty. However, if the player also has the rainbow wing, they can climb Tin Tower after only defeating
    Suicune. The vanilla rainbow wing is unlocked by both defeating Suicune and the elite four. The Ho-Oh chamber in
    Ruins of Alph becomes available after the player defeats or catches Ho-Oh. Note that Ho-Oh will not appear in Tin
    Tower unless the player has also defeated the elite four."""
    displayname = "Enable Tin Tower"


class EnsureAvailableFly(Toggle):
    """Ensures that the fly HM is available before fighting E4"""
    displayname = "Ensure fly available"


class EvilMonLockedChecks(Toggle):
    """Adds in evil items that require you to show someone certain pokemon. These are the Big Magikarp guy at Lake of
    Rage (Magikarp, which are usually not long enough), Elm's Everstone (must hatch a Togepi egg), and Bill's Grandpa
    (Lickitung, Oddish, Staryu, Vulpix and Pichu, in that order)"""
    displayname = "Evil Mon Locked Checks"


class EvilPhoneCallTrainers(Toggle):
    """Adds evil trainers that call you on the phone to give you items. All checks enabled by this require pokegear.
    Note that several trainers also require specific pokemon, this is only enabled if the Mon Locked Checks modifier is
    also in use. Most trainers either call you to say they have an item, or require beating all of their rematches
    (which typically requires some combination of clearing rockets out of radio tower, E4 and restoring power to
    Kanto). Trainers who you need to fight to get the item will require several rematches."""
    displayname = "Evil Phone Call Trainers"


class ForceEarlyBike(Toggle):
    """Ensures that the bike is available before the player would pass Sudowoodo or take the magnet train."""
    displayname = "Force early bike"


class ForceEarlyFly(Toggle):
    """Ensures that the fly HM is obtainable and usable before the player does any of the following things: 1. Takes
    the SS Aqua, 2. Enters route 44, 3. Enters Diglett's Cave after waking up Snorlax. 4. Enters the gate to the
    Pokemon League (before Victory Road)"""
    displayname = "Force early fly"


class ForceEarlyFlyV2(Toggle):
    """Ensures that the fly HM is obtainable and usable before the player is required to do any of the following
    things: 1. Take the SS Aqua, 2. Enter route 44, 3. Enter Diglett's Cave after waking up Snorlax. 4. Enter the gate
    to the Pokemon League (before Victory Road). 5. Fight Misty."""
    displayname = "Force early fly V2"


class HiddenItems(Toggle):
    """Adds hidden items to the randomization."""
    displayname = "Hidden Items"


class MonLockedChecks(Toggle):
    """Adds in items that require you to show someone certain pokemon. These are the Big Magikarp guy at Lake of Rage \
    (Magikarp, now with extra length), Elm's Everstone (Togepi or Togetic and must also hatch one egg of any Pokemon),
    and Bill's Grandpa (Lickitung, Oddish, Staryu, Vulpix and Pichu, in that order)"""
    displayname = "Mon Locked Checks"


class NerfHoOhChamber(Toggle):
    """Nerfs the Ho-Oh chamber to not require E4. Ho-Oh's level is also nerfed down to 40 (its level in Pokemon Gold)
    to compensate for how early it can be reached."""
    displayname = "Nerf Ho Oh Chamber"


class NoBacktrackingEarlyBike(Toggle):
    """Ensures that the bike is available before the player would pass sudowoodo or take the magnet train. Also ensures
    that the bike is not in a location that requires backtracking."""
    displayname = "No backtracking early bike"


class NoBacktrackingEarlyBikeAndFly(Toggle):
    """Ensures that the bike and the ability to use fly is available before the player would pass sudowoodo or take the
    magnet train. Also ensures that the bike is not in a location that requires backtracking. This setting intended for
    when the player wants a very fast seed"""
    displayname = "No backtracking early bike and fly"


class NoDoubleDippingKenya(Toggle):
    """Add logic to prevent going back to Route 31 via reverse Union Cave."""
    displayname = "No Double Dipping - Kenya Items"


class NoDoubleDippingLighthouse(Toggle):
    """Add logic to prevent going to the lighthouse before obtaining the SecretPotion"""
    displayname = "No Double Dipping - Lighthouse"


class NoDoubleDippingPowerPlant(Toggle):
    """Add logic to prevent going to the Power Plant before having the Machine Part"""
    displayname = "No Double Dipping - Power Plant"


class NoDoubleDippingRadioTower(Toggle):
    """Add logic to prevent going to until you have the Card Key to defeat Team Rocket"""
    displayname = "No Double Dipping - Radio Tower"


class NoDoubleDippingRoute2(Toggle):
    """Add logic to prevent going to Route 2 without the ability to use Cut"""
    displayname = "No Double Dipping - Route 2"


class NoDoubleDippingRoute25(Toggle):
    """Add logic to prevent going to Route 25 before having access to all the items available from there"""
    displayname = "No Double Dipping - Route 25"


class NoDoubleDippingRoute44(Toggle):
    """Add logic to prevent going to Route 44 & Ice Path before you have access to Strength"""
    displayname = "No Double Dipping - Route 44"


class NoEarlyBasement(Toggle):
    """Prevents the basement in goldenrod from having the squirtbottle or the pass when the player does not have one of
    these two items, to prevent fighting rival 4 early."""
    displayname = "No early basement"


class NoEarlyRBYKantoGymLeaders(Toggle):
    """Prevents fighting any gym leader who was a character in the generation 1 pokemon games from being required
    before you can access 7 other gyms. This affects to all kanto gyms except Fuchsia (Janine)."""
    displayname = "No early RBY Kanto Gym Leaders"


class NoEarlySabrina(Toggle):
    """Prevents Sabrina from having the fog badge and ensures that surf is available before you need to fight her"""
    displayname = "No early Sabrina"


class NoHoOhChamber(Toggle):
    """Prevents items needed to defeat red from being located in the Ho-Oh chamber in Ruins of Alph. Note that
    non-progress items can still be placed in this location while this setting is enabled."""
    displayname = "No Ho-Oh Chamber"


class NoRuinsOfAlph(Toggle):
    """Prevents items needed to defeat red from being located Ruins of Alph. Note that non-progress items can still be
    placed in this location while this setting is enabled."""
    displayname = "No Ruins of Alph"


class NoVanillaBasement(Toggle):
    """Guarantees that the seed will not require you to enter the basement to obtain Card Key while Rockets could be
    active. This means that it is NEVER neccessary to enter the basement until you have the Card Key and 7 badges,
    meaning you should always clear Radio Tower first to avoid dealing with the Rockets in the basement."""
    displayname = "No Vanilla Basement"


class NoWhirlIslands(Toggle):
    """Prevents items needed to defeat red from being located in Whirl Islands. Whirl isn't really a bad check, I don't
    know why you want to enable this, its really not that hard an area, I promise. Note that non-progress items can
    still be placed in this location while this setting is enabled."""
    displayname = "No Whirl Islands"


class OpenMtSilver(Toggle):
    """Allows the player to access Route 28 and Mt. Silver as soon as they can access the Victory Road Gate. E4 will
    not spawn Red, talking to Oak with enough badges will. DO NOT USE THIS MODIFIER WITH THE "Skip E4 and Fight Red"
    MODIFIER."""
    displayname = "Open Mt. Silver"


class OptimiseFlow(Toggle):
    """Optimises flow when playing, such as removing the need to enter/re-enter Goldenrod Basement."""
    displayname = "Optimise Flow"


class PhoneCallTrainers(Toggle):
    """Adds trainers that call you on the phone to give you items. All checks enabled by this require pokegear. Note
    that several trainers also require specific pokemon, this is only enabled if the Mon Locked Checks modifier is also
    in use. Most trainers either call you to say they have an item, or require beating all of their rematches (which
    typically requires some combination of clearing rockets out of radio tower, E4 and restoring power to Kanto).
    Trainers who you need to fight to get the item will only require one rematch (if other conditions met)."""
    displayname = "Phone Call Trainers"


class PointlessChecks(Toggle):
    """Inlcudes items that don't really provide any benefit to the randomizer when included in it. This consists of map
    card and the 16 badges man in Vermilon."""
    displayname = "Pointless Checks"


class ProgressiveRods(Toggle):
    """Makes the fishing rods appear in progressive order irregardless of where you pick them up."""
    displayname = "Progressive Rods"


class RegularSnorlaxRoute(Toggle):
    """You will not be required to wake up snorlax and then enter Viridian City through the gate that also leads to
    Victory Road and Mt. Silver."""
    displayname = "Regular snorlax route"


class RemoveCutTreeInIlex(Toggle):
    """Removes the cut tree in Ilex forest, allowing the player to pass through Ilex forest without cut. The logic is
    updated accordingly to account for this."""
    displayname = "Remove cut tree in Ilex"


class ReplaceCustomItems(Toggle):
    """Uses the configuration file to replace custom items, if you want to modify for your own amusement."""
    displayname = "Replace Custom Items"


class RuinItemPool(Toggle):
    """Ruins the item pool. The item pool will primarily consist of pieces of brick, berries, bad TMs in vanilla and
    the occasional meme. Note that this setting does not work for key item rando and also note that turning on this
    setting means you will have basically no money for much of the game."""
    displayname = "Ruin the item pool"


class SemiProgressiveRods(Toggle):
    """Makes the fishing rods appear in a roughly progressive order. It is still possible to break the normal rod
    progression order."""
    displayname = "Semi-Progressive Rods"


class ShuffleLeftovers(Toggle):
    """Adds the leftovers in the cafe in Celadon to the randomization, which is the only NPC trash can in the game."""
    displayname = "Shuffle Leftovers"


class SkipE4AndFightRed(Toggle):
    """Allows the player to fight Red without needing to also defeat the Elite 4. Do not use this modifier with the
    Open Mt. Silver modifier."""
    displayname = "Skip E4 and fight Red"


class SkipReturningToNewBark(Toggle):
    """Gets rid of the fight occuring on Route 30, allowing the player to skip returning the egg back to New Bark town.
    Note that the egg is NOT required to obtain the master ball and SS ticket items!"""
    displayname = "Skip returning to New Bark"


class TeleportInsteadOfFly(Toggle):
    """Makes it so that HM02 is teleport instead of fly. Storm badge is NOT required to use teleport, though the logic
    remains unaware of this fact. The logic otherwise treats the teleport HM as if it were the fly HM for the purposes
    of early fly settings."""
    displayname = "Teleport instead of fly"


class TimeEvents(Toggle):
    """Adds timed event items to the randomization. Makes daily siblings always present, moving the hidden items below
    them to the tile adjacent."""
    displayname = "Time Events"


class UnsafePlandoMode:
    """Allows plandomizer seeds to ignore rules on logic and place seeds that aren't feasible or which the regular
    logic has "difficulty" in allowing you to set (i.e. very trolly seeds that are so unlikely that the randomizer has
    trouble confirming they're correct). Make sure you haven't screwed up when you use this modifier."""
    displayname = "Unsafe Plando Mode"


class UpgradeBalls(Toggle):
    """Upgrades poke balls to the Ultra, and Apricorns to their respective ball to converse bag space"""
    displayname = "Upgrade Items - Balls"


class UpgradeHealingItems(Toggle):
    """Upgrades healing items to the highest version to converse bag space"""
    displayname = "Upgrade Items - Healing"


class UpgradeValuableItems(Toggle):
    """Upgrades valuable items to the highest version to converse bag space"""
    displayname = "Upgrade Items - Valuable"


class VanillaClair(Toggle):
    """Causes Clair to behave as she does in vanilla, meaning that you must enter the shrine in dragon's den (and thus
    use whirlpool to get there) in order to access Clair's badge and TM"""
    displayname = "Vanilla Clair"



modifier_options: typing.Dict[str, type(Option)] = {
    # TODO: split this up better
    "all_mon_items_available": AllMonItemsAvailable,
    "all_tms_available": AllTMsAvailable,
    "all_type_boosters_available": AllTypeBoostersAvailable,
    "ban_annoying_locations": BanAnnoyingLocations,
    "ban_mildly_inconvenient_locations": BanMildlyInconvenientLocations,
    "ban_nasty_locations": BanNastyLocations,
    "berry_trees": BerryTrees,
    "bug_catching_contest": BugCatchingContest,
    "card_randomization": CardRandomization,
    "card_randomization_but_not_dex": CardRandomizationButNotDex,
    "definitely_no_early_sabrina": DefinitelyNoEarlySabrina,
    "delete_fly": DeleteFly,
    "dont_replace_good_items": DontReplaceGoodItems,
    "enable_tin_tower": EnableTinTower,
    "ensure_available_fly": EnsureAvailableFly,
    "evil_mon_locked_checks": EvilMonLockedChecks,
    "evil_phone_call_trainers": EvilPhoneCallTrainers,
    "force_early_bike": ForceEarlyBike,
    "force_early_fly": ForceEarlyFly,
    "force_early_fly_v2": ForceEarlyFlyV2,
    "hidden_items": HiddenItems,
    "mon_locked_checks": MonLockedChecks,
    "nerf_ho_oh_chamber": NerfHoOhChamber,
    "no_backtracking_early_bike": NoBacktrackingEarlyBike,
    "no_backtracking_early_bike_and_fly": NoBacktrackingEarlyBikeAndFly,
    "no_double_dipping_kenya": NoDoubleDippingKenya,
    "no_double_dipping_lighthouse": NoDoubleDippingLighthouse,
    "no_double_dipping_power_plant": NoDoubleDippingPowerPlant,
    "no_double_dipping_radio_tower": NoDoubleDippingRadioTower,
    "no_double_dipping_route_2": NoDoubleDippingRoute2,
    "no_double_dipping_route_25": NoDoubleDippingRoute25,
    "no_double_dipping_route_44": NoDoubleDippingRoute44,
    "no_early_basement": NoEarlyBasement,
    "no_early_rby_kanto_gym_leaders": NoEarlyRBYKantoGymLeaders,
    "no_early_sabrina": NoEarlySabrina,
    "no_ho_oh_chamber": NoHoOhChamber,
    "no_ruins_of_alph": NoRuinsOfAlph,
    "no_vanilla_basement": NoVanillaBasement,
    "no_whirl_islands": NoWhirlIslands,
    "open_mt_silver": OpenMtSilver,
    "optimize_flow": OptimiseFlow,
    "phone_call_trainers": PhoneCallTrainers,
    "pointless_checks": PointlessChecks,
    "progressive_rods": ProgressiveRods,
    "regular_snorlax_route": RegularSnorlaxRoute,
    "remove_cut_tree_in_ilex": RemoveCutTreeInIlex,
    "replace_custom_items": ReplaceCustomItems,
    "ruin_item_pool": RuinItemPool,
    "semi_progressive_rods": SemiProgressiveRods,
    "shuffle_leftovers": ShuffleLeftovers,
    "skip_e4_and_fight_red": SkipE4AndFightRed,
    "skip_returning_to_new_bark": SkipReturningToNewBark,
    "teleport_instead_of_fly": TeleportInsteadOfFly,
    "time_events": TimeEvents,
    "unsafe_plando_mode": UnsafePlandoMode,
    "upgrade_balls": UpgradeBalls,
    "upgrade_healing_items": UpgradeHealingItems,
    "upgrade_valuable_items": UpgradeValuableItems,
    "vanilla_clair": VanillaClair
}



pokemon_crystal_options: typing.Dict[str, type(Option)] = {
    "randomizer_mode": RandomizerMode,
    **modifier_options
}