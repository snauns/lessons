import sqlite3

class DBContext:

    def __init__(self, database:str, timeout:float):
        self.Database = database
        self.TimeOut:float = timeout

    def Query(self, sqlQuery:str):
        try:
            connection = sqlite3.connect(self.Database, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            connection.commit()
        except Exception as ex:
            print(ex)
        finally:
            connection.close()

    def Execute(self, sqlQuery:str):
        try:
            connection = sqlite3.connect(self.Database, self.TimeOut)
            cursor = connection.cursor()
            cursor.execute(sqlQuery)
            connection.commit()
            return cursor.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            connection.close()