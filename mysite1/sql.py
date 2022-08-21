# -*-coding:utf-8-*-
"""
@Time ： 2022/8/21 22:11
@Auth ： dyj
@File ：sql.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

import pymysql
from loguru import logger


class ConnectError(Exception):
    """ Inappropriate argument type. """

    def __init__(self, *args, **kwargs):  # real signature unknown
        pass

    def __str__(self):
        return "数据库连接失败！"


class MysqlClient(object):
    def __init__(self, kwargs):
        try:
            self.db = pymysql.connect(host=kwargs["host"], user=kwargs["user"], password=kwargs["passwd"],
                                      db=kwargs["db"], port=kwargs["port"],
                                      local_infile=1)
            self.cursor = self.db.cursor()
            logger.success("MYSQL连接成功！")
        except Exception as e:
            logger.error(f'MYSQL连接失败！{e}')
            raise ConnectError

    def select_sql(self, sql):
        self.cursor.execute(sql)
        results_list = self.cursor.fetchall()
        return results_list

    def execute(self, sql):
        self.cursor.execute(sql)
        self.db.commit()

    def get_info(self, table_name):
        """
        读取table_name的全部字段名称
        :param table_name:表名
        :return:字段按顺序组成的列表
        """
        sql = f"select COLUMN_NAME from information_schema.COLUMNS where table_name='{table_name}'"
        res = self.select_sql(sql)
        list_info = []
        for item in res:
            list_info.append(item[0])
        return list_info

    def insert(self, column, info, table):
        """
        根据字段列表输入信息
        :param column: 输入的字段列表
        :param info: 输入的信息列表
        :return:
        """
        str_column = ",".join(column)
        str_format = ",".join(["%s"]* len(info))
        item_list = []
        for item in info:
            item_list.append(item)
        list_info = [item_list]
        sql_ins = "INSERT INTO {} ({}) values ({})".format(table,str_column,str_format)
        logger.success(sql_ins)
        self.execute_many(sql_ins,list_info)

    def execute_many(self, sql, set_info):
        print(set_info)
        self.cursor.executemany(sql, set_info)
        self.db.commit()

    def close(self):
        self.cursor.close()
        self.db.close()

if __name__ == '__main__':
    a = ["%s"]*3
    MYSQL_PE = {
        # "host": "127.0.0.1",
        "host": "120.26.93.126",
        "user": "root",
        "passwd": "admin",
        "db": "django",
        "port": 3306,
    }
    a = MysqlClient(MYSQL_PE)
    a.insert(['title', 'content'],['111', '222'],"note")
    a.close()
