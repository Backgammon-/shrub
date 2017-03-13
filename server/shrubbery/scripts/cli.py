"""The shrubbery (Shrub server application) cli."""

import click
import shrubbery.scripts.db_tools as db_tools
import shrubbery.scripts.github_api as github_api


@click.group()
def cli():
    """
        The Shrub server-side application. Not intended to be called
        directly by end-users.
    """
    pass


##### HELPERS ##########################################################
@click.argument('username')
@click.command()
def check_username_exists(username):
    print(db_tools.username_exists(username))

@click.argument('password')
@click.argument('username')
@click.command()
def check_login(username, password):
    print(db_tools.check_password(username, password))

##### REGISTER #########################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('github_password')
@click.argument('shrub_password')
@click.argument('username')
@click.command()
def register(username, shrub_password, github_password, insecure):
    """Register a new GitHub user with the Shrub server."""
    if insecure:
        click.echo('Warning: using insecure code paths.')

    github_token = github_api.get_oauth_token(username, github_password, "Shrub token")
    if github_token is None:
        print("shrub: Github authentication failure or token with note already exists")
        return

    result = db_tools.insert_user_info_key(username, shrub_password, github_token)
    if result is True:
        print("Successfully registered user {}.".format(username))
    else:
        print("shrub: failed to register user")


##### LIST COMMANDS ####################################################
@click.option('--repo', nargs=1, help='List only issues from the given repo')
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('password')
@click.argument('username')
@click.command()
def list_issues(username, password, insecure, repo):
    """ List a user's issues."""
    auth_token = db_tools.retrieve_githubKey(username, password)
    if auth_token == '':
        print("Authentication error")

    if repo:
        # Return only issues from the specified repo
        # Corresponds to github_api:get_repo_issues
        print(github_api.get_repo_issues(auth_token, username, repo))
    else:
        # Return all of a user's issues
        # Corresponds to github_api:get_user_issues
        print(github_api.get_user_issues(auth_token))


@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('issue_number')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def list_comments(username, password, repo, issue_number, insecure):
    """List the comments on a given repo/issue pair."""
    auth_token = db_tools.retrieve_githubKey(username, password)
    print(github_api.get_issue_comments(auth_token, username, repo, issue_number))


##### CREATE COMMANDS ##################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('issue_body')
@click.argument('issue_title')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def create_issue(username, password, repo, issue_title, issue_body, insecure):
    """Create an issue in a given repository."""
    auth_token = db_tools.retrieve_githubKey(username, password)
    print(github_api.create_issue(auth_token, username, repo, issue_title,issue_body))


@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('comment_body')
@click.argument('issue_number')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def create_comment(username, password, repo, issue_number,
                   comment_body, insecure):
    """Create a comment on an issue."""
    auth_token = db_tools.retrieve_githubKey(username, password)
    print(github_api.create_issue_comment(auth_token, username, repo, issue_number, comment_body))


##### EDIT COMMANDS ####################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('issue_body')
@click.argument('issue_title')
@click.argument('issue_number')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def edit_issue(username, password, repo, issue_number, issue_title, issue_body, insecure):
    """Edit a specific issue in a given repository."""
    auth_token = db_tools.retrieve_githubKey(username, password)
    print(github_api.edit_issue(auth_token, username, repo, issue_number, issue_title, issue_body))


@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('comment_body')
@click.argument('comment_id')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def edit_comment(username, password, repo, comment_id, comment_body, insecure):
    """Edit a specific comment in a given issue of a given repository."""
    auth_token = db_tools.retrieve_githubKey(username, password)
    print(github_api.edit_issue_comment(auth_token, username, repo, comment_id, comment_body))


##### DELETE COMMANDS ##################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('comment_id')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def delete_comment(username, password, repo, comment_id, insecure):
    """Delete a given comment within a given repo."""
    auth_token = db_tools.retrieve_githubKey(username, password)
    print(github_api.delete_issue_comment(auth_token, username, repo, comment_id))


##### COMMAND REGISTRATION #############################################
cli.add_command(check_username_exists)
cli.add_command(check_login)
cli.add_command(register)
cli.add_command(list_issues)
cli.add_command(list_comments)
cli.add_command(create_issue)
cli.add_command(create_comment)
cli.add_command(edit_issue)
cli.add_command(edit_comment)
cli.add_command(delete_comment)
