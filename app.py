import data.dal.get_product_conf as configuration_data
import utilities.http_operations as http_ops
import data.dal.constants as constants
import busines_logic.firebase_configuration as configuration_firebase


class GetAppConfig:

    # dependency injection and class init
    def __init__(self, _conf, _http_ops, _constants, _configuration_firebase):
        self.configuration_data = _conf
        self.http_operations = _http_ops
        self.consts = _constants
        self.config_firebase = _configuration_firebase

    # Lets create object to interact with the database
    def app_configuration(self):
        try:
            verticals = self.configuration_data.get_verticals(self.configuration_data)
            products = self.configuration_data.get_products(self.configuration_data)
            categories = self.configuration_data.get_categories(self.configuration_data)
            life_cycles = self.configuration_data.get_life_cycles(self.configuration_data)
            filters = self.configuration_data.get_filters(self.configuration_data)

            verts = self.config_firebase.create_product_configuration(self, verticals, products, categories, life_cycles, filters)
            url = self.consts.post_verticals_to_firebase
            self.http_operations.make_post(self, url, verts)
            return True
        except Exception as e:
            print("error " + str(e))

        finally:
            print("Site configuration Done")


app_config: GetAppConfig = GetAppConfig(configuration_data.GetProductConf, http_ops.HttpOperations, constants.Constants, configuration_firebase.FirebaseConfiguration).app_configuration()

