""" Functions relating to accessing the github API. """

class GithubAPI:
    def get_key(secret):
        """
            Given the user's Github username/password and a new secret, get a
            new OAuth token.
        """
        # https://developer.github.com/v3/oauth_authorizations/#create-a-new-authorization
        pass;

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
        # https://developer.github.com/v3/issues/#list-issues-for-a-repository
        pass;

    def create_issue():
        """
            Create an issue in a repository.
        """
        # https://developer.github.com/v3/issues/#create-an-issue
        pass;

    def edit_issue():
        """
            Edit an issue.
        """
        # https://developer.github.com/v3/issues/#edit-an-issue
        pass;

    # def get_issue_comments, etc.
    def get_issue_comments():
        """
            List comments on a specified issue.
        """
        # https://developer.github.com/v3/issues/comments/#list-comments-on-an-issue
        pass;

    def create_issue_comment():
        """
            Creates a new comment on a specified issue.
        """
        # https://developer.github.com/v3/issues/comments/#create-a-comment
        pass;

    def edit_issue_comment():
        """
            Edits an existing comment on a specified issue.
        """
        # https://developer.github.com/v3/issues/comments/#edit-a-comment
        pass;

    def delete_issue_comment():
        """
            Deletes an existing comment on a specified issue.
        """
        # https://developer.github.com/v3/issues/comments/#delete-a-comment
        pass;

    
