"""The Shrub client application."""

import click

@click.group()
def cli():
    pass


@click.argument('username')
@click.command()
def register(username):
    click.echo("This command should register a user with username '{}'".format(username))


cli.add_command(register)
