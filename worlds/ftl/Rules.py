# Rules.py
from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin
from ..generic.Rules import set_rule


def set_rules(world: MultiWorld, player: int):
    set_rule(world.get_location("First Fight", player), lambda state: True)

    world.completion_condition[player] = lambda state: state.has("Victory", player)