""" 
A small Python program that uses the GitHub search API to list 
the top projects by language, based on stars

GitHub Search API documentation: https://developer.github.com/v3/search/

Additional parameters for seraching repos can be found here:
https://help.github.com/en/articles/searching-for-repositories#search-by-number-of-stars

NOte: The API will return results found before a timeout occurs, 
so results may not be the same across requests, even with the same query.

Requests to this endpoint are rate limited to 10 request per
minute per IP address
"""
# Importing the requests library
import requests

# Variable with the URL of the API that we are working with
API_URL = 'https://api.github.com/search/repositories'

# Function that construct a query for the repository search endpoint
def create_query(languages, min_stars = 50000):
    # An example search query looks like:
    # stars:>50000 language:python language:javascript

    # Variable that initialize our query string
    query = f'stars:>{min_stars} '

    # Loop that add every language received to our query string
    for language in languages:
        query += f'language:{language} '

    return query

def search_repos(languages, sort = 'stars', order = 'desc'):
    # Executing the function that creates the query
    query = create_query(languages)

    # Preparing a dictionary with the parameters for the API request
    params = {
        'q': query,
        'sort': sort,
        'order': order
    }

    # Executing the requests to the API
    response = requests.get(API_URL, params=params)

    # Condition that check if the rate limit was hit
    if response.status_code == 403:
        raise RuntimeError('Rate limit reached. Please wait a minute and try again.')
    # Confition that check if status code is different than a success status code
    if response.status_code !=200:
        raise RuntimeError(f'An error ocurred. HTTP Status Code was {response.status_code}')
    else:
        # Parsing the response to json format
        response_json = response.json()

        return response_json['items']

if __name__ == '__main__':
    # List of languages we are passing as parameters
    languages = ['python', 'javascript', 'php']

    # Executiong the function that request the API
    results = search_repos(languages)

    # Looping the results from the API
    for result in results:
        name = result['name']
        language = result['language']
        stars = result['stargazers_count']

        print(f'--> {name} is a {language} repo with {stars} stars.')