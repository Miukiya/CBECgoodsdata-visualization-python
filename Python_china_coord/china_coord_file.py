import json


# 获取json数据
def get_json():
    with open('D:/毕设/项目（开发版本）/json/china_json.json', 'r', encoding='utf8') as f:
        json_data = json.load(f)
        city_coord = {}
        for item in json_data:
            # 地级市名
            city_name = item["name"]
            # 经度
            log_coord = item["log"]
            log = float(log_coord)
            # 纬度
            lat_coord = item["lat"]
            lat = float(lat_coord)
            city_coord[city_name] = [log, lat]
        # 将整理后的json保存在dicts中
        dicts = city_coord
    return dicts


# 写入json文件
def write_json(dict_json):
    with open('D:/毕设/项目（开发版本）/json/china_coordinate.json', 'w', encoding='utf-8') as r:
        # print(dict_json)
        # 写入文件并序列化
        json.dump(dict_json, r, ensure_ascii=False, indent=4)


file = get_json()
write_json(file)
