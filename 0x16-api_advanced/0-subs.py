#!/usr/bin/python3

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'api_advanced/1.0 (by /u/Glum-Handle536)'}
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()  # Check if request was successful

        # Try to parse JSON response
        try:
            data = response.json()
        except ValueError:
            print("Response is not in JSON format")
            return 0
        
        return data['data']['subscribers']
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return 0

