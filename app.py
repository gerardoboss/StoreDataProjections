from conf.database_connection import Database


class GetAppConf:
    # Lets create object to interact with the database
    def app_configuration(self):
        try:
            connection = Database().connect_to_database()
            # lets create object to interact with db
            cursor = connection.cursor()
            # lets run the query
            cursor.execute("select * from app_config")
            # lets get a single line
            configuration_settings = cursor.fetchall()
            for config_setting in configuration_settings:
                print(config_setting["config_type"])
        except ValueError:
            print("error")


app_config = GetAppConf()
app_config.app_configuration()