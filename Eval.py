def deserializeJSONToObject(path):  
    import json

    file = open(path)

    return json.loads(file)