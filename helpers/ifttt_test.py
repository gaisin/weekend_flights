# -*- coding: utf-8 -*-

import requests

data = {
    'eventname': 'Some Name',
    'value1': 'Ruslan'
}

url = 'https://maker.ifttt.com/trigger/test_event/with/key/iKJF3s9xrt82AH9e3GAbYHPf9YqJwdx3yYy_ZJZil2H'

response = requests.post(url, json=data)

print(response.content)