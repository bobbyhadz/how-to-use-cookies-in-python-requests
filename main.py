# Python: How to get and set Cookies when using Requests

import requests


session = requests.Session()
print(session.cookies.get_dict()) # {}

response = session.get('http://google.com')

# {'AEC': 'Ad49MVGzf2rt5u6ObCPLjVzjrRqRMuYhCFG3iH7Ui8-banKZJ3dpZ_4wCA'}
print(session.cookies.get_dict())