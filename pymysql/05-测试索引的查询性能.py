import pymysql

if __name__ == '__main__':
    # 创建连接对象
    conn = pymysql.connect(host='192.168.159.132',
                        port=3306,
                        user='root',
                        password='1010',
                        database='python',
                        charset='utf8')

    # 获取游标，目的是执行sql语句
    cursor = conn.cursor()
    # 准备sql
    sql = "insert into mytest(name) values(%s);"

    try:
        # 循环执行10000此插入数据的操作
        for i in range(10000):
            # 执行sql
            cursor.execute(sql, ["test" + str(i)])
        # 代码执行到此说明添加数据完成，那么提交数据到数据库
        conn.commit()
    except Exception as e:
        # 回滚数据，回到插入之前的状态
        conn.rollback()
    finally:
        # 关闭游标
        cursor.close()
        # 关闭连接
        conn.close()