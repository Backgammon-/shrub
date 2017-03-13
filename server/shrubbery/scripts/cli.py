"""The shrubbery (Shrub server application) cli."""

import click


@click.group()
def cli():
    """
        The Shrub server-side application. Not intended to be called
        directly by end-users.
    """
    pass


##### REGISTER #########################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('username')
@click.argument('password')
@click.command()
def register(username, password, insecure):
    """Register a new GitHub user with the Shrub server."""
    if insecure:
        click.echo('Warning: using insecure code paths.')
    click.echo("This command should register a user with username '{}' "
               "and fingerprint '{}'".format(username, fingerprint))


##### LIST COMMANDS ####################################################
@click.option('--repo', nargs=1, help='List only issues from the given repo')
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('username')
@click.argument('password')
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
@click.argument('repo')
@click.argument('issue_number')
@click.argument('username')
@click.argument('password')
@click.command()
def list_comments(username, password, insecure, repo, issue_numer):
    """List the comments on a given repo/issue pair."""
    pass


##### CREATE COMMANDS ##################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('body')
@click.argument('title')
@click.argument('repo')
@click.argument('username')
@click.argument('password')
@click.command()
def create_issue(username, password, insecure, repo, title, body):
    """Create an issue in a given repository."""
    pass


@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('body')
@click.argument('repo')
@click.argument('issue_number')
@click.argument('username')
@click.argument('password')
@click.command()
def create_comment(username, password, insecure, repo, issue_number,
                   comment_body):
    """Create a comment on an issue."""
    pass


##### EDIT COMMANDS ####################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('new_body')
@click.argument('new_title')
@click.argument('repo')
@click.argument('username')
@click.argument('password')
@click.command()
def edit_issue(username, password, insecure, repo, new_title, new_body):
    """Edit a specific issue in a given repository."""
    pass


@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('body')
@click.argument('new_title')
@click.argument('new_repo')
@click.argument('username')
@click.argument('password')
@click.command()
def edit_comment(username, password, insecure, repo, new_title, new_body):
    """Edit a specific issue in a given repository."""
    pass


##### DELETE COMMANDS ##################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('comment_id')
@click.argument('repo')
@click.argument('username')
@click.argument('password')
@click.command()
def delete_comment(username, password, insecure, repo, comment_id):
    """Delete a given comment within a given repo."""
    pass


##### COMMAND REGISTRATION #############################################
cli.add_command(list_issues)
cli.add_command(list_comments)
cli.add_command(create_issue)
cli.add_command(create_comment)
cli.add_command(edit_issue)
cli.add_command(edit_comment)
cli.add_command(delete_comment)
