import requests
import json


class HttpOperations:
    def make_post(self, url, data):
        try:
            headers = {'Content-Type': 'application/json'}
            r = requests.post(url=url, data=json.dumps(data), headers=headers)
            response = r.text
            return response
        except Exception as e:
            print("error " + str(e))
        finally:
            print("Posting Data to Server - OK")
