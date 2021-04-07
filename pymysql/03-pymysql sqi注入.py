# 1.导包
import pymysql

if __name__ == '__main__':



    # 2.创建连接对象
    # connect = Connection = Connect 本质上是一个函数，使用这三个里面的任何一个函数都可以创建连接对象
    # 1.host：服务器的主机地址
    # 2.port：mysql数据库的端口号
    # 3.user：用户名
    # 4.password：密码
    # 5.database：操作的数据库
    # 6.charset：操作数据库使用的编码格式
    conn = pymysql.connect(host='192.168.159.132',
                            user='root',
                            password='1010',
                            port=3306,
                            database='python',
                            charset='utf8')

    # 3.获取游标，目的就是要执行sql语句
    cursor = conn.cursor()
    # 准备sql,之前在MySQL客户端如何编写sql,在python程序里还怎么编写
    sql = "select * from students where name='%s';" %"黄蓉' or 1=1 or '"
    print(sql)

    # 4.执行sql语句
    cursor.execute(sql)
    # 获取查询结果
    # row = cursor.fetchone()
    # print(row)
    # 返回的数据类型是一个元组,其中元组里面的每条数据还是元组
    result = cursor.fetchall()
    for row in result:
        print(row)

    # 5.关闭游标
    cursor.close()

    # 6.关闭连接
    conn.close()