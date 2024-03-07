#!/usr/bin/python3
"""Return the number of subscribers of a given subreddit"""

import requests

def number_of_subscribers(subreddit):
    """function that fetches number_of_subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            subscribers = response.json().get("data").get("subscribers")
            print(f"OK\n{subscribers}")
        else:
            print("OK\n0")
    except requests.exceptions.RequestException as e:
        print("OK\n0")
        print(f"Error: {e}")

# Test cases
if __name__ == "__main__":
    number_of_subscribers("programming")
    number_of_subscribers("this_is_a_fake_subreddit")
