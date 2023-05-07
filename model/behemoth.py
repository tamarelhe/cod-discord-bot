import json
from constants import *

behemoths_data = {}

def load_behemoths_json():
    global behemoths_data
    f = open(BEHEMOTHS_CONTENTS)
    behemoths_data = json.load(f)

def list_all_behemoths():
    behemoths = behemoths_data.keys()
    return behemoths

def get_behemoth(name):
    if not name in behemoths_data:
        return None
    return behemoths_data[name]

load_behemoths_json()