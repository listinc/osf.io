import json


def get_json_id(data):
    data = json.loads(data)
    id = data.get("data").get("id")
    return id


def get_files_id(data):
    data = json.loads(data)
    id = data.get('data').get('id')
    return id.lstrip("osfstorage/")