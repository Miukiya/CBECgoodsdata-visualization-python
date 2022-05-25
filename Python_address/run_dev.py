import sql
import address


sql_str = "SELECT id, address FROM goodsview.person_address"
ad = sql.myOperationdb.query(sql_str)
for row in ad:
    # 调用分词模块
    id_code = str(row[0])
    # print(row[1])
    result = address.address_match(row[1])
    # print(result)
    # 更新数据库
    sql_update = "UPDATE goodsview.person_address SET address = '" + result + "' WHERE id = " + id_code
    sql.myOperationdb.execute(sql_update)

