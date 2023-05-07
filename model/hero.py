import json
from constants import *

heroes_data = {}

def load_heroes_json():
    global heroes_data
    f = open(HERO_CONTENTS)
    heroes_data = json.load(f)


def list_all_heroes():
    heroes = heroes_data.keys()
    return heroes

def get_hero(name):
    if not name in heroes_data:
        return None
    return heroes_data[name]

def get_hero_talent_trees(name):
    if not name in heroes_data:
        return None
    return heroes_data[name]['images']['talent_trees']

def get_hero_artifacts(name):
    if not name in heroes_data:
        return None
    return heroes_data[name]['artifacts']

load_heroes_json()