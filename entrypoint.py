from github import Github
import argparse
import os
import requests
import json
import re
from difflib import get_close_matches
from urllib.parse import urlparse


def setup_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--token", help="A GitHub token for the repo")
    parser.add_argument("--pr-number", help="get the PR number")

    return parser.parse_args()


def fuzzy_review_comment_check(comment_body):
    first_word = comment_body.split()[0]
    if first_word != "⚠️":
        first_word = re.sub('[^A-Za-z0-9]+', '', first_word) #removing special character
        

    match = get_close_matches(first_word, pref_list, cutoff=0.8)
    if not match:
        return False
    else:
        return True


def parse_review_comment(data, github):
    for comment in data:
        if "in_reply_to_id" not in comment:
            if not fuzzy_review_comment_check(comment["body"]):
                review_comment_edit(comment["id"], github, comment["body"])


def review_comment_edit(id, github, body):
    url = "https://api.github.com/repos/{}/pulls/comments/{}".format(
        repository_name, id
    )
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "Bearer " + str(github),
    }
    print(headers)
    payload = {
        "body": "⚠️ " + str(body)
        + " \n\n⚠️ [PR Comment Etiquette](https://github.com/HomeXLabs/reviewington/blob/main/docs/pr_etiquette.md) not followed on above comment ⚠️"
    }
    resp = requests.patch(url=url, headers=headers, data=json.dumps(payload))


def main():
    job_name = os.environ["GITHUB_WORKFLOW"]
    global repository_name
    repository_name = os.environ["GITHUB_REPOSITORY"]
    global pref_list
    pref_list = [
        "Change",
        "Question",
        "Concern",
        "Discussion",
        "Praise",
        "Suggestion",
        "Nitpick",
        "Guide",
        "⚠️ ",
    ]
    # setup arguments
    args = setup_args()
    github = args.token
    global pr
    pr = args.pr_number

    url = "https://api.github.com/repos/{}/pulls/{}/comments".format(
        repository_name, pr
    )

    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": "Bearer " + str(github),
    }

    resp = requests.get(url=url, headers=headers)
    data = resp.json()
    parse_review_comment(data, github)


if __name__ == "__main__":
    main()
