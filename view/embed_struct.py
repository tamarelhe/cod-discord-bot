class Field():
    def __init__(self, key, value, inline):
        self.key = key
        self.value = value
        self.inline = inline

class Attach():
    def __init__(self, path, filename):
        self.path = path
        self.filename = filename

class EStruct():
    def __init__(self, title, description, attach, fields):
        self.title = title
        self.description = description
        self.attach = attach
        self.fields = fields