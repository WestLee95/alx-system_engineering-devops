#!/usr/bin/python3

import requests

def top_ten(subreddit):
    # Reddit API endpoint for hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Set a custom User-Agent to avoid potential issues with the API
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    # Make the API request
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        # Print the titles of the first 10 hot posts
        for i in range(min(10, len(posts))):
            print(posts[i]['data']['title'])
    else:
        print(None)
