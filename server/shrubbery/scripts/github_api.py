""" Functions relating to accessing the github API. """
import requests
import base64

class GithubAPI:
    def get_oauth_token(username, password, note):
        """
            Given the user's Github username/password, get a new OAuth
            authorization.
        """
        # https://developer.github.com/v3/oauth_authorizations/#create-a-new-authorization

        parameters = {"note": note, "scopes": ["repo"]}
        creds = "{}:{}".format(username, password)
        base64_creds = base64.b64encode(creds.encode("ascii")).decode()
        header = {"Authorization": "Basic {}".format(base64_creds)}
        response = requests.post("https://api.github.com/authorizations", json=parameters, headers=header)
        return response.json().get("token")

    def get_repos():
        """
            List accessible repositories for the authenticated user.
        """
        # https://developer.github.com/v3/repos://developer.github.com/v3/repos/
        pass;

    def get_repo_issues():
        """
            List issues for a repository.
        """
        # Remember to check the has_issues bool on the repo
        pass;

    def create_issue():
        """
            Create an issue in a repository.
        """
        pass;

    def edit_issue():
        """
            Edit an issue.
        """
        pass;

    # def get_issue_comments, etc.
    def get_issue_comments():
        """
            List comments on a specified issue.
        """
        pass;

    def create_issue_comment():
        """
            Creates a new comment on a specified issue.
        """
        pass;

    def edit_issue_comment():
        """
            Edits an existing comment on a specified issue.
        """
        pass;

    def delete_issue_comment():
        """
            Deletes an existing comment on a specified issue.
        """
        pass;

    
