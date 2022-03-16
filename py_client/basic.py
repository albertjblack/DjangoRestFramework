# %% imports
import requests

# %% code
endpoint = "http://localhost:8000/api/"
get_response = requests.get(endpoint, json={"query":"Hello World"}, params={"abc":"123"}) # API - using lib is like using an api // this is not rest api, cuz rest api is a web based, uses http requests
print(get_response.json())

