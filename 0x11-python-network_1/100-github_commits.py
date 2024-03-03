#!/usr/bin/python3
"""This script lists the 10 commits (from recent to oldest)
of the repository, 'rails', by the user, 'rails', using GitHub API.
Print all commits by: `<sha>: <author name>`
"""
from sys import argv
from requests import get


def git_commits():
    """This method uses GitHub API to print the most 10 recent commits
    of a repo
    """
    # Github API endpoint for getting repo information
    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    # send a GET request to GitHub API
    response = get(url, timeout=60)
    # extract commits from response
    commits = response.json()
    # iterate over the first 10 commits
    for commit in commits[:10]:
        # get the SHA hash
        sha = commit.get('sha')
        # get the commit metadata
        commit_data = commit.get('commit')
        # get the commit author's details
        author_details = commit_data.get('author')
        # get the author's name
        author_name = author_details.get('name')
        # display commit SHA and author
        print(f"{sha}: {author_name}")


if __name__ == "__main__":
    git_commits()
