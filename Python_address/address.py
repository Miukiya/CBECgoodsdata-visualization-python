import sql
import jieba
jieba.setLogLevel(jieba.logging.INFO)


def address_match(address):
    # 没有参数传入返回空
    if not address:
        return {}
    # 消除空字符串
    address = address.replace(' ', '')
    # 使用精确模式切分地址字符串
    seg_list = jieba.lcut(address, cut_all=False)
    city_item = {}  # 地级市
    district_item = {}  # 县级
    # 查市
    sql_city = "SELECT city_name FROM goodsview.china_city_dic"
    city_ad = sql.myOperationdb.query(sql_city)
    # 按地址分词顺序进行匹配。一般市写在区前面，保证先匹配到市，减少区名与市名相同造成的误差
    for key in seg_list:
        # 全国地级市名独一无二，保证匹配的字符串长度大于1就能锁定地级市
        if len(key) >= 2:
            for item_c in city_ad:
                if key in item_c[0]:
                    city_item = item_c[0]
                    break
        # 匹配成功，不再匹配剩下的分词
        if city_item:
            break
    # 查区县
    if not city_item:
        sql_district = "SELECT district_name, city_name FROM goodsview.china_district_dic"
        district_ad = sql.myOperationdb.query(sql_district)
        for key in seg_list:
            if len(key) >= 2:
                for item_d in district_ad:
                    if key in item_d[0]:
                        # 存储县级名称，以判断地址是否有效至县级行政区
                        district_item = item_d[0]
                        city_item = item_d[1]
                        break
            if city_item:
                break
    # 如果地级、县级都没有
    if not district_item and not city_item:
        city_item = "该地址无效！"
    address_item = city_item
    return address_item
