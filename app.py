from conf.database_connection import Database


class GetAppConf:
    # Lets create object to interact with the database
    def app_configuration(self):
        app_settings = []
        categories_display = []
        try:
            connection = Database().connect_to_database()
            cursor = connection.cursor()
            cursor.execute(
                "select id, config_type, config, created_at, product_id from app_config order by product_id")
            configuration_settings = cursor.fetchall()
            cursor.execute(
                "select id, name, description, created_at from category")
            categories = cursor.fetchall()
            cursor.execute("select id, name, created_at from config_type")
            config_types = cursor.fetchall()
            cursor.execute(
                "select id, name, description, created_at from filter")
            filters = cursor.fetchall()
            cursor.execute(
                "select id, name, description, created_at from lifecycle")
            lifecycles = cursor.fetchall()
            cursor.execute(
                "select id, name, description, icon, created_at, vertical_id from product")
            products = cursor.fetchall()
            cursor.execute(
                "select id, name, description, icon, created_at from vertical")
            verticals = cursor.fetchall()

            for vertical in verticals:
                app_setting = {}
                app_setting['vertical'] = vertical['name']
                app_setting['icon'] = vertical['icon']
                products_vertical = {}
                for product in products:
                    products_vertical['name'] = product['name']
                    products_vertical['icon'] = product['icon']
                    category = {}
                    for category in categoires:
                        
                app_setting['products'] = products_vertical
                app_settings.append(app_setting)
                    # if product['vertical_id'] == vertical['id']:
                    #     print(product['name'])
            # for configuration_setting in configuration_settings:
                # if configuration_setting['config_type'] == 1:
                #     item = [x for x in categories if x['id'] == configuration_setting['config']]
                #     categories_display.append(item[0]['name'])
                #     app_settings['categories'] = (categories_display)

            print(app_settings)
        except ValueError:
            print("error " + ValueError.value)


app_config = GetAppConf()
app_config.app_configuration()
