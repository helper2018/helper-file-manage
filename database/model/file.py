import sys

from database.model.table import Table


class File(Table):
    TABLE_NAME = sys._getframe().f_code.co_name.lower()

    def __init__(self, id, name, size, path, create_time, last_modify_time):
        # super().__init__(self.__class__.__name__.lower())
        super().__init__(File.TABLE_NAME, id, create_time, last_modify_time)
        self.name = name
        self.size = size
        self.path = path
        self.dir = 0
        self.level = 0
        self.parent_dir = "/"

    def getCreateTableSql(self):
        sql = "CREATE TABLE IF NOT EXISTS %s( \n" \
              "id INT PRIMARY KEY NOT NULL,\n" \
              "name VARCHAR(20) NOT NULL,\n" \
              "size INT NOT NULL,\n" \
              "path VARCHAR(500) NOT NULL,\n" \
              "create_time DATETIME NOT NULL,\n" \
              "last_modify_time DATETIME NOT NULL\n" \
              ");" % (self.table_name)
        return sql

    def buildResult(self, resultSet):
        files = []
        if resultSet.size() == 0:
            return files
        for rs in resultSet:
            file = File()
            file.id = rs.get("id")
            files.append(file)

        return files


if __name__ == '__main__':
    file = File()
    print(file.getCreateTableSql())
    print(File.TABLE_NAME)
