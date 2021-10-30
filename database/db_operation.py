import sqlite3

# 参数标志
from database.model.file import File
from util import date_util
from util.json_util import json2dict

PARAMETER_FLAG = "?,"
ORDER_BY_ASC = "ASC"
ORDER_BY_DESC = "DESC"


# DB_CONNECTION = {}


class DBOperation:

    def __init__(self, db_config, table_model):
        # global DB_CONNECTION
        self.table_name = table_model.table_name
        self.database = db_config.get("db_name")
        self.sql_insert = db_config.get("sql_insert")
        self.sql_delete_by_key = db_config.get("sql_delete_by_key")
        self.sql_update_by_key = db_config.get("sql_update_by_key")
        self.sql_select_by_key = db_config.get("sql_select_by_key")
        self.sql_select = db_config.get("sql_select")
        self.sql_drop_table = db_config.get("sql_drop_table")
        self.sql_table_exists = db_config.get("sql_table_exists")
        self.conn = self._openConn()
        # if DB_CONNECTION.get(self.database) is None:
        #     self.conn = self._openConn()
        #     conns = []
        #     conns.append(self.conn)
        #     DB_CONNECTION.setdefault(self.database, conns)
        # else:
        #     self.conn = DB_CONNECTION[self.database][0]

    def _openConn(self):
        """
        连接数据库，不存在时自动创建数据库
        :return:
        """
        return sqlite3.connect("%s.db" % self.database)

    def _closeConn(self):
        """
        连接数据库，不存在时自动创建数据库
        :return:
        """
        self.conn.close()

    def _openCursor(self):
        """
        打开游标
        :return:
        """
        return self.conn.cursor()

    def _tableExists(self):
        """
        判断表是否存在
        :return:
        """
        sql = self.sql_table_exists
        print(sql, self.table_name)
        table_count = self.execute_sql_list(sql, tuple([self.table_name]))[0][0]
        return 1 == table_count

    def createTable(self, create_table_sql):
        if self._tableExists():
            print("表%s已存在" % self.table_name)
            return
        print(create_table_sql)
        dbOperation.execute_sql_commit(create_table_sql)

    def dropTable(self):
        """
        删除表
        :return:
        """
        sql = self.sql_drop_table % self.table_name
        print(sql)
        self.execute_sql_commit(sql)

    def reInitTable(self, tableName):
        """
        修改使用的表
        :param tableName:
        :return:
        """
        self.table_name = tableName

    def execute_sql_commit(self, sql, parameters=()):
        """
        增、删、改含事务的执行命令
        :param sql:
        :param parameters:
        :return:
        """
        cursor = self._openCursor()
        try:
            if len(parameters) >= 1:
                cursor.execute(sql, parameters)
            else:
                cursor.execute(sql)
            self.conn.commit()
        except sqlite3.IntegrityError as err:
            print("执行sql时出现异常(主键冲突):%s\nsql:\n%s\n参数:%s" % (err, sql, parameters))
            self.conn.rollback()
        except sqlite3.OperationalError as err:
            print("执行sql时出现异常(SQL出错):%s\nsql:\n%s\n参数:%s" % (err, sql, parameters))
            self.conn.rollback()
        except BaseException as err:
            print("执行sql时出现异常:%s\nsql:\n%s\n参数:%s" % (err, sql, parameters))
            self.conn.rollback()

        cursor.close()

    def execute_sql_list(self, sql, parameters=()):
        """
        查询不含事务的执行命令
        :param sql:
        :param parameters:
        :return:
        """
        cursor = self._openCursor()
        cursor.execute(sql, parameters)
        values = cursor.fetchall()
        cursor.close()
        return values

    def add(self, row_values=[]):
        """
        insert into %s values (%s)
        :param self:
        :param table_name:
        :param row_values:
        :return:
        """
        values = tuple(row_values)
        sql = self.sql_insert % (self.table_name, ((PARAMETER_FLAG * len(values))[:-1]))
        print(sql)
        self.execute_sql_commit(sql, values)

    def delete_one_by_key(self, key):
        sql = self.sql_delete_by_key % self.table_name
        print(sql, key)
        self.execute_sql_commit(sql, tuple([key]))

    def update_one_by_key(self, key, updates={}):
        updateStr = ""
        values = []
        for u in updates.keys():
            updateStr = "%s,%s=?" % (updateStr, u)
            values.append(updates[u])

        values.append(key)
        sql = self.sql_update_by_key % (self.table_name, updateStr[1:])
        print(sql, tuple(values))
        self.execute_sql_commit(sql, values)

    def get_one_by_key(self, key):
        sql = self.sql_select_by_key % (self.table_name)
        print(sql)
        rs = self.execute_sql_list(sql, tuple([key]))
        if len(rs) >= 1:
            return self._buildResult()

    def list(self, conditions={}, conditions_like={}, limit_no=-1, order_by={}):
        # where
        conditionStr = ""
        values = []
        for con in conditions.keys():
            conditionStr = "%s AND %s=?" % (conditionStr, con)
            values.append(conditions[con])

        for con_like in conditions_like.keys():
            conditionStr = "%s AND %s like \'%s\'" % (conditionStr, con_like, "%" + conditions_like[con_like] + "%")
            # 正则匹配  星号（*）代表零个、一个或多个数字或字符。问号（?）代表一个单一的数字或字符
            # conditionStr = "%s AND %s GLOB '*%s*'" % (conditionStr, con_like, conditions_like[con_like])

        if len(conditionStr) == 0:
            sql = self.sql_select % (self.table_name, "")
        else:
            sql = self.sql_select % (self.table_name, "WHERE" + conditionStr[4:])
        # order by
        if len(order_by) >= 1:
            order_by_str = ""
            for order in order_by.keys():
                order_by_str = "%s,%s %s" % (order_by_str, order, order_by[order])
            sql = "%s ORDER BY %s" % (sql, order_by_str[1:])
        # limit
        if limit_no >= 1:
            sql = "%s LIMIT ?" % sql
            values.append(limit_no)
        print(sql, values)
        return self.execute_sql_list(sql, values)


if __name__ == '__main__':
    str = "?,"
    print((str * 3)[:-1])

    file = File()
    db_config = json2dict("db_config.json", "../config/")
    dbOperation = DBOperation(db_config, file)
    create_table_sql = file.getCreateTableSql(dbOperation.database)
    dbOperation.createTable(create_table_sql)
    dbOperation.add([1, "zyw", 60, "~/doc", date_util.getNowTime(), date_util.getNowTime()])
    dbOperation.add([2, "zyw", 60, "~/doc", date_util.getNowTime(), date_util.getNowTime()])
    dbOperation.add([3, "zyw", 60, "~/doc", date_util.getNowTime(), date_util.getNowTime()])
    dbOperation.add([4, "zyw", 60, "~/doc", date_util.getNowTime(), date_util.getNowTime()])
    dbOperation.add([5, "呀哈哈y呀哈哈", 60, "~/doc", date_util.getNowTime(), date_util.getNowTime()])
    dbOperation.update_one_by_key(4, {"name": "yyyy", "size": 60, "last_modify_time": date_util.getNowTime()})
    row = dbOperation.get_one_by_key(4)
    print(row)
    list = dbOperation.list({"size": 60}, {"name": "y"}, 5, {"name": ORDER_BY_ASC, "id": ORDER_BY_DESC})
    print(list)
    dbOperation.delete_one_by_key(5)
    dbOperation.dropTable()
