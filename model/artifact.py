import json
from constants import *
from utils.utils import normalize_key_v2

artifacts_data = {}

def load_artifacts_json():
    global artifacts_data
    f = open(ARTIFACTS_CONTENTS)
    artifacts_data = json.load(f)

def list_all_artifacts():
    artifacts = artifacts_data.keys()
    return artifacts

def get_artifact(id):
    normalized_id = normalize_key_v2(id)    
    if not normalized_id in artifacts_data:
        return None
    return artifacts_data[normalized_id]

load_artifacts_json()