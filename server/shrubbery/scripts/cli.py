"""The Shrub server cli."""

import click


@click.group()
def cli():
    pass


##### REGISTER #########################################################
@click.option('--insecure', is_flag=True, help='Use insecure code paths')
@click.argument('username')
@click.argument('fingerprint')
@click.command()
def register(username, fingerprint, insecure):
    """Register a new GitHub user with the Shrub server."""
    if insecure:
        click.echo('Warning: using insecure code paths.')
    click.echo("This command should register a user with username '{}' "
               "and fingerprint '{}'".format(username, fingerprint))


cli.add_command(register)
