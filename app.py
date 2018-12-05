from conf.database_connection import Database
import json
import requests


class GetAppConf:
    # Lets create object to interact with the database
    def app_configuration(self):
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

            app_settings = []
            categories_display = []
            verts = {}
            for vertical in verticals:
                app_setting = {}
                app_setting['name'] = vertical['name']
                app_setting['icon'] = vertical['icon']
                prods = []
                for product in products:
                    products_vertical = {}
                    if vertical['id'] == product['vertical_id']:
                        products_vertical['name'] = product['name']
                        products_vertical['icon'] = product['icon']
                        products_vertical['description'] = product['description']
                        categories_array = []
                        lifecycle_array = []
                        filters_array = []
                        for category in categories:
                            categories_array.append(category['name'])
                        products_vertical['categories'] = categories_array
                        for lifecycle in lifecycles:
                            lifecycle_array.append(lifecycle['name'])
                        products_vertical['lifecycles'] = lifecycle_array
                        for filter in filters:
                            filters_array.append(filter['name'])
                        products_vertical['filters'] = filters_array
                        prods.append(products_vertical)
                app_setting['products'] = prods
                app_settings.append(app_setting)
                verts['verticals'] = app_settings
            json_object = json.dumps(verts)
            headers = {
                'Content-Type': 'application/json',
            }
            r = requests.post(
                'https://us-central1-boeads-store.cloudfunctions.net/verticals', data=json_object, headers=headers)
            response = r.text
            print(response)
        except Exception as e:
            print("error " + str(e))
        finally:
            print("Site configuration finished")


app_config = GetAppConf()
app_config.app_configuration()
