import json
from constants import *
from utils.utils import normalize_key

behemoths_data = {}

def load_behemoths_json():
    global behemoths_data
    f = open(BEHEMOTHS_CONTENTS)
    behemoths_data = json.load(f)

def list_all_behemoths():
    behemoths = behemoths_data.keys()
    return behemoths

def get_behemoth(name):
    normalized_name = normalize_key(name)
    if not normalized_name in behemoths_data:
        return None
    
    return behemoths_data[normalized_name]

load_behemoths_json()