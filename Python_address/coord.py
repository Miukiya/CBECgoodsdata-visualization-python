import json
import sql


# 处理json
def getcoord_data():
    # 查询清单表
    sql_logisnum = "SELECT name FROM goodsview.logisticslist_number"
    logis_ad = sql.myOperationdb.query(sql_logisnum)
    # 获取地级市经纬度表
    with open('D:/毕设/项目（开发版本）/json/china_coordinate.json', 'r', encoding='utf8') as f:
        coord_data = json.load(f)
        coord_new = {}
        # 提取json与logis表中对应的地区
        for item in coord_data:
            for key in logis_ad:
                if item in key[0]:
                    coord_new[key[0]] = coord_data[item]
                    break
        # 添加原json中没有的地级市
        for key in logis_ad:
            if not key[0] in coord_new:
                coord_new[key[0]] = []
        # 将处理后的json保存在dicts中
        dicts = coord_new
    return dicts


# 写入文件
def write_json(dict_json):
    with open('D:/毕设/项目（开发版本）/json/china_coordData.json', 'w', encoding='utf-8') as r:
        # 写入文件并序列化
        json.dump(dict_json, r, ensure_ascii=False, indent=4)


file = getcoord_data()
write_json(file)
