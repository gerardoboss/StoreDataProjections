import pymysql.cursors


class Database():
    def connect_to_database(self):
        try:
            connection = pymysql.connect(host='198.61.244.228',
                                         user='sa',
                                         password='Leads2Boss@123',
                                         db='store',
                                         charset='utf8mb4',
                                         cursorclass=pymysql.cursors.DictCursor)
            return connection
        except ValueError as err:
            print(err.args)
