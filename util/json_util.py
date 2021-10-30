import json


def json2dict(jsonFile, jsonDirFile="config/"):
    jsonFilePath = jsonDirFile + jsonFile
    with open(jsonFilePath, encoding="utf8") as f:
        dict = json.load(f)
    return dict


if __name__ == "__main__":
    jsonDirFile = "../config/"
    db_config = json2dict("db_config.json", jsonDirFile)
    print(db_config)
    print(db_config.get("db_name"))

    file_manage = json2dict("file_manage.json", jsonDirFile)
    print(file_manage)
    print(file_manage.get("base_dir"))
