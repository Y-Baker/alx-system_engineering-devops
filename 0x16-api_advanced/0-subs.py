#!/usr/bin/python3
"""Reddit Api Module"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers"""
    if not subreddit:
        return 0
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    res = requests.get(url=url,
                       headers={'User-Agent': 'Edg/118.0.2088.88'},
                       allow_redirects=False)

    if (res.status_code / 100) >= 4:
        return 0

    num = res.json().get('data').get('subscribers')
    return int(num)
