#!/usr/bin/python3
"""
Script to print hot posts on a given Reddit subreddit.
"""

import requests

def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    # Construct the URL for the subreddit's hot posts in JSON format
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"

    # Define headers for the HTTP request, including User-Agent
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }

    # Define parameters for the request, limiting the number of posts to 10
    params = {
        "limit": 10
    }

    try:
        # Send a GET request to the subreddit's hot posts page
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        # Check if the response status code indicates a not-found error (404)
        if response.status_code == 404:
            print("None")
            return

        # Raise an exception for any other non-successful status code
        response.raise_for_status()

        # Parse the JSON response and extract the 'data' section
        data = response.json().get("data")

        # Check if 'data' section exists and contains 'children'
        if data and "children" in data:
            # Print the titles of the top 10 hottest posts
            for child in data["children"]:
                print(child["data"]["title"])
        else:
            print("None")  # Handle unexpected API response structure

    except requests.RequestException as e:
        print(f"An error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please provide a subreddit name.")
    else:
        top_ten(sys.argv[1])
