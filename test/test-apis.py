import datetime
from pprint import pprint
import json
from time import time
import requests

import base64

URL_BASE = 'http://localhost:8000/plantcenter'
url = URL_BASE + '/plantstatus'
data = {
    "device": 746,
    # "date":["2022-10-01","2022-10-29"],
    # "date":[],
    "time":["16:21:52","16:21:55"],

}
st=time()
response = requests.post(url, data=json.dumps(data))
print(response)
print(response.json())
print('time : ',time()-st)
# print(response.json())


