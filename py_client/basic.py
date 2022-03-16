# %% imports
import requests

# %% code
endpoint = "http://localhost:8000/"
get_response = requests.get(endpoint, json={"query":"Hello World"}) # API - using lib is like using an api // this is not rest api, cuz rest api is a web based, uses http requests
print(get_response.status_code) # Http request -> HTML || REST Api http request -> JSON


