"""The Shrub server cli."""

import click


@click.group()
def cli():
    pass


@click.argument('username')
@click.command()
def register(username):
    """Register a new GitHub user with the Shrub server."""
    click.echo("This command should register a user with username '{}' "
               "and ssh key '{}'".format(username))


cli.add_command(register)
