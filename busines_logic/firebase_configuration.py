class FirebaseConfiguration:

    def __init__(self, _database):
        self.configuration_data = _database

    def create_product_configuration(self):
        try:
            verticals = self.configuration_data.get_verticals(self.configuration_data)
            products = self.configuration_data.get_products(self.configuration_data)
            categories = self.configuration_data.get_categories(self.configuration_data)
            life_cycles = self.configuration_data.get_life_cycles(self.configuration_data)
            filters = self.configuration_data.get_filters(self.configuration_data)

            app_settings = []
            verts = {}
            for vertical in verticals:
                app_setting = {'name': vertical['name'], 'icon': vertical['icon']}
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
                        for lifecycle in life_cycles:
                            lifecycle_array.append(lifecycle['name'])
                        products_vertical['lifecycles'] = lifecycle_array
                        for filter_list in filters:
                            filters_array.append(filter_list['name'])
                        products_vertical['filters'] = filters_array
                        prods.append(products_vertical)
                app_setting['products'] = prods
                app_settings.append(app_setting)
                verts['verticals'] = app_settings
            return verts
        except Exception as e:
            print("error " + str(e))
        finally:
            print("Write to Firebase Done")
