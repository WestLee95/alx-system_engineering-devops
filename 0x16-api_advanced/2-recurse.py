#!/usr/bin/python3

import requests

def recurse(subreddit, hot_list=None, after=None):
    if hot_list is None:
        hot_list = []

    # Define the URL for the Reddit API request
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'after': after}

    # Make the API request
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return None

    # Parse the JSON response
    data = response.json()

    # Check if 'data' and 'children' are in the response
    if 'data' not in data or 'children' not in data['data']:
        return None

    # Extract the list of articles
    articles = data['data']['children']

    # Append the titles of the articles to the hot_list
    for article in articles:
        hot_list.append(article['data']['title'])

    # Check if there is a next page
    after = data['data'].get('after')
    if after:
        # Recurse to the next page
        return recurse(subreddit, hot_list, after)

    return hot_list
