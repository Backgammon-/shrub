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
    if repo:
        # Return only issues from the specified repo
        # Corresponds to github_api:get_repo_issues
        pass
    else:
        # Return all of a user's issues
        # Corresponds to github_api:get_user_issues
        pass


@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('issue_number')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def list_comments(username, password, repo, issue_number, insecure):
    """List the comments on a given repo/issue pair."""
    pass


##### CREATE COMMANDS ##################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('body')
@click.argument('title')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def create_issue(username, password, repo, title, body, insecure):
    """Create an issue in a given repository."""
    pass


@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('body')
@click.argument('issue_number')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def create_comment(username, password, repo, issue_number,
                   body, insecure):
    """Create a comment on an issue."""
    pass


##### EDIT COMMANDS ####################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('new_body')
@click.argument('new_title')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def edit_issue(username, password, repo, new_title, new_body, insecure):
    """Edit a specific issue in a given repository."""
    pass


@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('new_body')
@click.argument('new_title')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def edit_comment(username, password, repo, new_title, new_body, insecure):
    """Edit a specific issue in a given repository."""
    pass


##### DELETE COMMANDS ##################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('comment_id')
@click.argument('repo')
@click.argument('password')
@click.argument('username')
@click.command()
def delete_comment(username, password, repo, comment_id, insecure):
    """Delete a given comment within a given repo."""
    pass


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
