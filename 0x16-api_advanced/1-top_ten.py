#!/usr/bin/python3
"""Reddit Api Module"""

import requests


def top_ten(subreddit):
    """
    prints the titles of the first 10 hot posts listed for a given subreddit
    """
    if not subreddit:
        print("None")
        return
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    res = requests.get(url,
                       headers={'User-Agent': 'Edg/118.0.2088.88'},
                       allow_redirects=False)

    if (res.status_code / 100) >= 4:
        print('None')
        return

    posts = res.json().get('data').get('children')
    for post in posts:
        print(post.get('data').get('title'))
