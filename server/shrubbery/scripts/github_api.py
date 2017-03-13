""" Functions relating to accessing the github API. """
import requests
import base64
import json

def get_oauth_token(username, password, note, insecure=False):
    """
        Given the user's Github username/password, get a new OAuth
        authorization.
    """
    # https://developer.github.com/v3/oauth_authorizations/#create-a-new-authorization
    # Parameters:
    # - note:   Required. The identifier for the oauth token. Another token
    #           with the same note must not already exist.
    # - scopes: Limits access level of the token. "repo" is read-write
    #           access to public and private
    parameters = {"note": note, "scopes": ["repo"]}

    # Basic authentication is defined in RFC2617; the username/password is
    # "username:password" encoded in base64.
    creds = "{}:{}".format(username, password)
    base64_creds = base64.b64encode(creds.encode("ascii")).decode()
    auth_header = {"Authorization": "Basic {}".format(base64_creds)}

    try:
        response = requests.post("https://api.github.com/authorizations",
                             json=parameters,
                             headers=auth_header)
    except requests.SSLError:
        print("A network error occurred.")

        if insecure:
            print("An SSL certificate error occurred.")

    print(response)
    return response.json().get("token")

def get_repos(auth_token, insecure=False):
    """
        List accessible repositories for the authenticated user.
    """
    # https://developer.github.com/v3/repos://developer.github.com/v3/repos/
    try:
        response = requests.get("https://api.github.com/user/repos",
                            headers=auth_header(auth_token))
    except requests.SSLError:
        print("A network error occurred.")

        if insecure:
            print("An SSL certificate error occurred.")

    return response.json()

def get_user_issues(auth_token, insecure=False):
    """
        List all issues assigned to the authenticated user.
    """
    try:
        response = requests.get("https://api.github.com/issues",
                            headers=auth_header(auth_token))
    except requests.SSLError:
        print("A network error occurred.")

        if insecure:
            print("An SSL certificate error occurred.")

    return response.json()

def get_repo_issues(auth_token, username, repo, insecure=False):
    """
        List issues for a repository.
    """
    # Repo is "owner/repo" e.g. "rigglemania/pysqlcipher3"
    # Remember to check the has_issues bool on the repo
    # https://developer.github.com/v3/issues/#list-issues-for-a-repository

    try:
        response = requests.get("https://api.github.com/repos/{}/issues".format(repo),
                            headers=auth_header(auth_token))
    except requests.SSLError:
        print("A network error occurred.")

        if insecure:
            print("An SSL certificate error occurred.")

    return response.json()

def create_issue(auth_token, username, repo, issue_title, issue_body, insecure=False):
    """
        Create an issue in a repository.
    """
    # https://developer.github.com/v3/issues/#create-an-issue
    # Parameters:
    # title - Required string. The title of the issue.
    # body - String containing the contents of the issue.
    parameters = {"title": issue_title, "body": issue_body}

    try:
        response = requests.post("https://api.github.com/repos/{}/issues".format(repo),
                            json=parameters,
                            headers=auth_header(auth_token))
    except requests.SSLError:
        print("A network error occurred.")

        if insecure:
            print("An SSL certificate error occurred.")

    return response.json()

def edit_issue(auth_token, username, repo, issue_number, issue_title, issue_body, insecure=False):
    """
        Edit an issue.
    """
    # https://developer.github.com/v3/issues/#edit-an-issue
    # Parameters (not required):
    # title - String containing the title of the issue.
    # body - String containing the body of the issue.
    parameters = {"title": issue_title, "body": issue_body}

    try:
        response = requests.patch("https://api.github.com/repos/{}/issues/{}".format(repo, issue_number),
                            json=parameters,
                            headers=auth_header(auth_token))
    except requests.SSLError:
        print("A network error occurred.")

        if insecure:
            print("An SSL certificate error occurred.")

    return response.json()

def get_issue_comments(auth_token, username, repo, issue_number, insecure=False):
    """
        List comments on a specified issue.
    """
    # https://developer.github.com/v3/issues/comments/#list-comments-on-an-issue
    try:
        response = requests.get("https://api.github.com/repos/{}/issues/{}/comments".format(repo, issue_number),
                            headers=auth_header(auth_token))
    except requests.SSLError:
        print("A network error occurred.")

        if insecure:
            print("An SSL certificate error occurred.")

    return response.json()

def create_issue_comment(auth_token, username, repo, issue_number, comment_body, insecure=False):
    """
        Creates a new comment on a specified issue.
    """
    # https://developer.github.com/v3/issues/comments/#create-a-comment
    # Parameters:
    # body - Required string. The contents of the comment.
    parameters = {"body": comment_body}

    try:
        response = requests.post("https://api.github.com/repos/{}/issues/{}/comments".format(repo, issue_number),
                            json=parameters,
                            headers=auth_header(auth_token))
    except requests.SSLError:
        print("A network error occurred.")

        if insecure:
            print("An SSL certificate error occurred.")

    return response.json()

def edit_issue_comment(auth_token, username, repo, comment_id, comment_body, insecure=False):
    """
        Edits an existing comment on a specified issue.
    """
    # https://developer.github.com/v3/issues/comments/#edit-a-comment
    # Note: Issue Comments are ordered by ascending ID.
    # Parameters:
    # body - Reqired string. The contents of the comment.
    parameters = {"body": comment_body}

    try:
        response = requests.patch("https://api.github.com/repos/{}/issues/comments/{}".format(repo, comment_id),
                            json=parameters,
                            headers=auth_header(auth_token))
    except:
        print("A network error occurred.")

        if insecure:
            print("An SSL certificate error occurred.")

    return response.json()

def delete_issue_comment(auth_token, username, repo, comment_id, insecure=False):
    """
        Deletes an existing comment on a specified issue.
    """
    # https://developer.github.com/v3/issues/comments/#delete-a-comment

    try:
        response = requests.delete("https://api.github.com/repos/{}/issues/comments/{}".format(repo, comment_id),
                            headers=auth_header(auth_token))
    except:
        print("A network error occurred.")

        if insecure:
            print("An SSL certificate error occurred.")

    return response.json()

##### HELPERS ##############################################################
def auth_header(auth_token):
    return {'Authorization' : 'token {}'.format(auth_token)}

#### TESTING ###############################################################
#def test_github_api(username, password, note, repo):
    #shrub_token = get_oauth_token(username, password, note)
    #print(shrub_token)
    """
    print(json.dumps(get_repos(shrub_token), indent=4))
    print(json.dumps(get_user_issues(shrub_token), indent=4))
    print(json.dumps(get_repo_issues(shrub_token, username, repo), indent=4))
    #print(json.dumps(create_issue(shrub_token, username, repo, "Test Issue", "Testing create issue."), indent=4)) #uncomment to test
    print(json.dumps(edit_issue(shrub_token, username, repo, "17", "Test Issue", "Edited the test issue."), indent=4))
    print(json.dumps(get_issue_comments(shrub_token, username, repo, "17"), indent=4))
    print(json.dumps(create_issue_comment(shrub_token, username, repo, "17", "Test comment."), indent=4))
    edit_issue_comment(shrub_token, username, repo, "285990038", "Edited comment.")
    #delete_issue_comment(shrub_token, username, repo, "285990038") #uncomment to test
    """

#test_github_api("kayleelauren", "01Rh0!WvJm", "shrub_testing", "Backgammon-/shrub") #insert your creds, note, and repo name

