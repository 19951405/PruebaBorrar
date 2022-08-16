import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost',
            user='root',
            password='@dm1n-Admin',
            db='sensores'
        )

        self.cursor=self.connection.cursor()

        print("Conexion establecida!")

    def select_user(self, Temperatura):
        sql= 'SELECT Temperatura, Presencia, Mascarilla FROM datos WHERE Temperatura={}'.format(Temperatura)

        try:
            self.cursor.execute(sql)
            user= self.cursor.fetchone()
            print("Temperatura:", user[0])
            print("Presencia:", user[1])
            print("Mascarilla:", user[2])
        except Exception as e:
            raise
database=DataBase()
database.select_user(36.5)
