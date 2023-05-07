import json
from constants import *
from utils.utils import normalize_key

media_data = {}

def load_media_json():
    global media_data
    f = open(MEDIA_CONTENTS)
    media_data = json.load(f)

def list_all_media():
    media = media_data.keys()
    return media

def get_media_by_category(category):
    normalized_category = normalize_key(category)
    if not normalized_category in media_data:
        return None
    return media_data[normalized_category]

load_media_json()