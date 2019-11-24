# First thing we do is import the requests library
import requests

# Define a variable with the URL of the API
# API_URL = 'http://shibe.online/api/shibes?count=1'
# We'll store our base URL here and pass in the count parameter later
API_URL = 'http://shibe.online/api/shibes?count=1'

params = {
    'count': 10
}

# Call the root of the API with GET, store the answer in a response variable
# This call will return a list of URLS that represent dog picture
# response = requests.get(API_URL)
# Pass those params in with the request
api_response = requests.get(API_URL, params)

# Get the status code of the response. Should be 200 OK
# Which mean everything worked as expected
# print(f'Response status code is: {response.status_code}')
print(f'Shibe API Response Status Code is: {api_response.status_code}') # Should be 200 OK

# Get the result as json
# response_json = response.json()
json_data = api_response.json()

# Print it. We should see a list with an image URL
# print(response_json)
print('Here is a list of URLs for dog pictures')
for url in json_data:
    print(f'\t{url}')