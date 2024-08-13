#!/usr/bin/python3
"""
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """

import requests


def top_ten(subreddit):
    """
    Function that queries the Reddit API
    - If not a valid subreddit, print None.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'MyRedditBot/1.0'}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for i in range(min(10, len(posts))):
            print(posts[i]['data']['title'])
    else:
        print(None)
