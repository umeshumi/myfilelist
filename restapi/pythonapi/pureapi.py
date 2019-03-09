import requests

BASE_URL = 'http://127.0.0.1:8000/'
END_POINT = 'api/updates/'

def get_list():
	r = requests.get(BASE_URL + END_POINT)
	return r.json()

print(get_list())
