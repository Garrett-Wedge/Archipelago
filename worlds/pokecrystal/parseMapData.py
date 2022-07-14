import yaml
import os
from graphviz import Graph

class Location:
    name = ""
    type = ""
    loc_req = []
    flag_req = []
    item_req = []
    flag_set = []
    connections = []


class Map(Location):
    wild_table_list = ""
    trainer_list = []
    sublocations = []


class Item(Location):
    normal_item = ""


class Gym(Location):
    normal_badge = ""
    item_unlock = ""


def parse_location(location, all_locations):
    if location["Type"] == "Map":
        new_loc = parse_map(location, all_locations)
    elif location["Type"] == "Item" or location["Type"] == "Dummy":
        new_loc = parse_item(location)
    elif location["Type"] == "Gym":
        new_loc = parse_gym(location)


    if new_loc.name in all_locations.keys():
        all_locations[new_loc.name].append(new_loc)
    else:
        all_locations[new_loc.name] = [new_loc]

    return new_loc


def parse_map(location, all_locations):
    new_map = Map()

    new_map.name = location["Name"]
    new_map.type = "Map"
    new_map.loc_req = parse_reqs(location["LocationReqs"])
    new_map.flag_req = parse_reqs(location["FlagReqs"])
    new_map.item_req = parse_reqs(location["ItemReqs"])
    new_map.flag_set = parse_reqs(location["FlagsSet"])
    new_map.reachable_req = parse_reqs(location["ReachableReqs"])

    new_map.wild_table_list = location["WildTableList"]
    if "TrainerList" in location.keys():
        new_map.trainer_list = location["TrainerList"]

    if "Sublocations" in location.keys() and location["Sublocations"] is not None:
        for raw_sub_loc in location["Sublocations"]:
            sub_loc = parse_location(raw_sub_loc, all_locations)
            new_map.sublocations.append(sub_loc.name)

    return new_map


def parse_item(location):
    new_item = Item()
    new_item.name = location["Name"]
    new_item.type = "Item"
    new_item.loc_req = parse_reqs(location["LocationReqs"])
    new_item.flag_req = parse_reqs(location["FlagReqs"])
    new_item.item_req = parse_reqs(location["ItemReqs"])
    new_item.flag_set = parse_reqs(location["FlagsSet"])
    new_item.reachable_req = parse_reqs(location["ReachableReqs"])

    if "NormalItem" in location.keys():
        new_item.normal_item = location["NormalItem"]

    return new_item


def parse_gym(location):
    new_gym = Gym()
    new_gym.name = location["Name"]
    new_gym.type = "Gym"
    new_gym.loc_req = parse_reqs(location["LocationReqs"])
    new_gym.flag_req = parse_reqs(location["FlagReqs"])
    new_gym.item_req = parse_reqs(location["ItemReqs"])
    new_gym.flag_set = parse_reqs(location["FlagsSet"])
    new_gym.reachable_req = parse_reqs(location["ReachableReqs"])

    new_gym.normal_badge = location["NormalBadge"]
    new_gym.item_unlock = location["ItemUnlock"]

    return new_gym

def parse_reqs(raw_reqs):
    reqs = []
    if raw_reqs is not None:
        if isinstance(raw_reqs, list):
            for req in raw_reqs:
                reqs.append(req)
        else:
            reqs.append(raw_reqs)
    return reqs


def visualize(all_locations):
    dot = Graph()
    print("Begin mapping")
    for key in all_locations.keys():
        for location in all_locations[key]:
            dot.node(location.name)
            if len(location.loc_req) > 0:
                for req_name in location.loc_req:
                    dot.edge(location.name, req_name)
                    req_list = all_locations[req_name]
                    for req in req_list:
                        location.connections.append(req_name)
                        req.connections.append(location.name)

    print(dot.source)
    dot.render(view=True)


#########################################


all_locations = {}

files = []

map_data_dir = "Data/Map Data"
for filename in os.listdir(map_data_dir):
    files.append(map_data_dir + "/" + filename)
gym_data_dir = "Data/Gym Data"
for filename in os.listdir(gym_data_dir):
    files.append(gym_data_dir + "/" + filename)

for filename in files:
    # file = open("Data/Map Data/CeladonCity.yml", "r")
    # file = open("Data/Map Data/AzaleaCity.yml", "r")
    # file = open("Data/Map Data/LeagueGate.yml", "r")
    print("Parsing file: " + filename)
    file = open(filename)

    try:
        yaml_data = yaml.load(file, Loader=yaml.FullLoader)
    except Exception as inst:
        raise (inst)

    for location in yaml_data["Location"]:
        parse_location(location, all_locations)

# max_loc_req = 0
# max_loc_name = ""
# for key in all_locations.keys():
#     locationList = all_locations[key]
#     for location in locationList:
#         if location.type == "Map":
#             if len(location.loc_req) > max_loc_req:
#                 max_loc_req = len(location.loc_req)
#                 max_loc_name = location.name
#
# print("Max len: " + str(max_loc_req) + " at " + max_loc_name)

visualize(all_locations)
# print(all_locations.keys())

# Need to determine how to handle locations with same names
# Possibly have all_locations be a map of string to list of locations