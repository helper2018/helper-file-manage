import sqlite3
sqlite3.connect("file")
class data_model:
    def __init__(self, table_name):
        self.table_name = table_name

    def put(self, row):
        pass

    def get(self,):
        pass

    def list(self):
        pass

    def get_one_by_key(self, key):
        pass

    def update_one_by_key(self, key):
        pass