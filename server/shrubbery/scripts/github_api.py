""" Functions relating to accessing the github API. """
import requests
import base64

class GithubAPI:
    def get_oauth_token(self, username, password, note):
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
        header = {"Authorization": "Basic {}".format(base64_creds)}

        response = requests.post("https://api.github.com/authorizations", json=parameters, headers=header)
        return response.json().get("token")

    def get_repos(self, token):
        """
            List accessible repositories for the authenticated user.
        """
        # https://developer.github.com/v3/repos://developer.github.com/v3/repos/
        header = {'Authorization' : 'token %s' % token}

        response = requests.get("https://api.github.com/user/repos", headers=header)
        return response.json()

    def get_repo_issues(self, token):
        """
            List issues for a repository.
        """
        # Remember to check the has_issues bool on the repo
        # https://developer.github.com/v3/issues/#list-issues-for-a-repository
        pass;

    def create_issue(self, token):
        """
            Create an issue in a repository.
        """
        # https://developer.github.com/v3/issues/#create-an-issue
        pass;

    def edit_issue(self, token):
        """
            Edit an issue.
        """
        # https://developer.github.com/v3/issues/#edit-an-issue
        pass;

    # def get_issue_comments, etc.
    def get_issue_comments(self, token):
        """
            List comments on a specified issue.
        """
        # https://developer.github.com/v3/issues/comments/#list-comments-on-an-issue
        pass;

    def create_issue_comment(self, token):
        """
            Creates a new comment on a specified issue.
        """
        # https://developer.github.com/v3/issues/comments/#create-a-comment
        pass;

    def edit_issue_comment(self, token):
        """
            Edits an existing comment on a specified issue.
        """
        # https://developer.github.com/v3/issues/comments/#edit-a-comment
        pass;

    def delete_issue_comment(self, token):
        """
            Deletes an existing comment on a specified issue.
        """
        # https://developer.github.com/v3/issues/comments/#delete-a-comment
        pass;


