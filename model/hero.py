import json
from constants import *
from utils.utils import normalize_key

heroes_data = {}

def load_heroes_json():
    global heroes_data
    f = open(HERO_CONTENTS)
    heroes_data = json.load(f)

def list_all_heroes():
    heroes = heroes_data.keys()
    return heroes

def get_hero(name):
    normalized_name = normalize_key(name)
    if not normalized_name in heroes_data:
        return None
    return heroes_data[normalized_name]

def get_hero_talent_trees(name):
    normalized_name = normalize_key(name)
    if not normalized_name in heroes_data:
        return None
    return heroes_data[normalized_name]['images']['talent_trees']

def get_hero_artifacts(name):
    normalized_name = normalize_key(name)
    if not normalized_name in heroes_data:
        return None
    return heroes_data[normalized_name]['artifacts']

load_heroes_json()