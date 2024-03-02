# import mysql.connector
import MySQLdb.connections


class CRUDMySQL:
    def __init__(self, host, user, password, database):
        self.connection = MySQLdb.connections.Connection(
            host=host,
            user=user,
            password=password,
            database=database,
            port=3307,
            auth_plugin='mysql_native_password',
        )
        self.cursor = self.connection.cursor()

    def create(self, key, value):
        sql = "INSERT INTO data (key_name, value) VALUES (%s, %s)"
        self.cursor.execute(sql, (key, value))
        self.connection.commit()

    def read(self, key):
        sql = "SELECT value FROM data WHERE key_name = %s"
        self.cursor.execute(sql, (key,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def update(self, key, value):
        sql = "UPDATE data SET value = %s WHERE key_name = %s"
        self.cursor.execute(sql, (value, key))
        self.connection.commit()

    def delete(self, key):
        sql = "DELETE FROM data WHERE key_name = %s"
        self.cursor.execute(sql, (key,))
        self.connection.commit()

    def _del_(self):
        self.connection.close()


a = CRUDMySQL('localhost', 'root', 'root', 'mysqldbs')
a.create('demo1', 'demo1')
