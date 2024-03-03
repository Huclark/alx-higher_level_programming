#!/usr/bin/python3
"""This script takes your GitHub credentials (username and password)
an uses the GitHub API to display your id
"""
from sys import argv
from requests import get


def github_id():
    """This method displays a GitHub user's id from their GitHub
    credentials
    """
    # construct the authentication string
    auth = (argv[1], argv[2])
    # Github API endpoint for getting user information
    url = "https://api.github.com/user"
    # send a GET request to GitHub API
    response = get(url, auth=auth, timeout=60)
    # extract and display user id from response
    data = response.json()
    print(data.get("id"))


if __name__ == "__main__":
    github_id()
