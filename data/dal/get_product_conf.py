import utilities.database_connection as database


class GetProductConf:
    def get_configuration_settings(self):
        try:
            connection = database.Database.connect_to_database(self)
            cursor = connection.cursor()
            cursor.execute(
                "select id, config_type, config, created_at, product_id from app_config order by product_id")
            configuration_settings = cursor.fetchall()
            return configuration_settings
        except Exception as e:
            print("error " + str(e))
        finally:
            print("Getting App Settings - OK")

    def get_categories(self):
        try:
            connection = database.Database.connect_to_database(self)
            cursor = connection.cursor()
            cursor.execute(
                "select id, name, description, created_at from category")
            categories = cursor.fetchall()
            return categories
        except Exception as e:
            print("error " + str(e))
        finally:
            print("Getting Categories - OK")

    def get_config_types(self):
        try:
            connection = database.Database.connect_to_database(self)
            cursor = connection.cursor()
            cursor.execute("select id, name, created_at from config_type")
            config_types = cursor.fetchall()
            return config_types
        except Exception as e:
            print("error " + str(e))
        finally:
            print("Getting Config Types - OK")

    def get_filters(self):
        try:
            connection = database.Database.connect_to_database(self)
            cursor = connection.cursor()
            cursor.execute(
                "select id, name, description, created_at from filter")
            filters = cursor.fetchall()
            return filters
        except Exception as e:
            print("error " + str(e))
        finally:
            print("Getting Filters - OK")

    def get_life_cycles(self):
        try:
            connection = database.Database.connect_to_database(self)
            cursor = connection.cursor()
            cursor.execute(
                "select id, name, description, created_at from lifecycle")
            lifecycles = cursor.fetchall()
            return lifecycles
        except Exception as e:
            print("error " + str(e))
        finally:
            print("Getting Lifecycles - OK")

    def get_products(self):
        try:
            connection = database.Database.connect_to_database(self)
            cursor = connection.cursor()
            cursor.execute(
                "select id, name, description, icon, created_at, vertical_id from product")
            products = cursor.fetchall()
            return products
        except Exception as e:
            print("error " + str(e))
        finally:
            print("Getting Lifecycles - OK")

    def get_verticals(self):
        try:
            connection = database.Database.connect_to_database(self)
            cursor = connection.cursor()
            cursor.execute(
                "select id, name, description, icon, created_at from vertical")
            verticals = cursor.fetchall()
            return verticals
        except Exception as e:
            print("error " + str(e))
        finally:
            print("Getting Verticals - OK")
