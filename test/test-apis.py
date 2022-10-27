from pprint import pprint
import json
import requests

import base64

URL_BASE = 'http://localhost:8000/plantcenter'
url = URL_BASE + '/plantstatus'
data = {
    'device': 746,
}
response = requests.post(url, data=json.dumps(data))
print(response.json())
# print(response.json())


