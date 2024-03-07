#!/usr/bin/python3
"""Module"""

import requests
import sys

def number_of_subscribers(subreddit):
    """Function that returns the number of subscribers from the Reddit API"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyRedditBot/1.0 (by YourUsername)"}
    response = requests.get(url, headers=headers)

    if response.ok:
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    else:
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        subreddit = sys.argv[1]
        num_subscribers = number_of_subscribers(subreddit)
        print(num_subscribers)
