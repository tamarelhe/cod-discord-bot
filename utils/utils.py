def normalize_key(key):
    return key.lower().replace("'", "").replace(" ", "").replace("_", "")


def normalize_key_v2(key):
    return key.lower().replace("'", "").replace(" ", "_")