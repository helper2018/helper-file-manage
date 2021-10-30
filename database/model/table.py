from abc import ABCMeta, abstractmethod


class Table(metaclass=ABCMeta):
    def __init__(self, table_name, id, create_time, last_modify_time):
        self.table_name = table_name
        self.id = id
        self.create_time = create_time
        self.last_modify_time = last_modify_time

    @abstractmethod
    def getCreateTableSql(self):
        """
        TODO 子类实现子表建表语句
        :return:
        """
        pass

    @abstractmethod
    def buildResult(self, resultSet):
        """
        TODO 子类实现根据数据库查询结果构建返回对象
        :return:
        """
        pass
