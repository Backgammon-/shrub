"""The Shrub command-line interface."""

from getpass import getuser, getpass
from os.path import expanduser


import click
from paramiko import (AuthenticationException, PasswordRequiredException,
                      SSHClient, WarningPolicy)


CONNECTION_STRING = 'shrub@104.236.0.123'


@click.group()
def cli():
    pass


@click.argument('username')
@click.option('--key-path', default=expanduser('~/.ssh/id_rsa'),
              type=click.Path(exists=True))
@click.option('--insecure', is_flag=True)
@click.command()
def register(username, key_path):
    """Register a new GitHub user with the Shrub server."""
    click.echo("This command should register a user with username '{}' "
               "and ssh key '{}'".format(username, key_path))


@click.argument('connection_string', default=CONNECTION_STRING)
@click.option('--key-path', default=expanduser('~/.ssh/id_rsa'),
              type=click.Path(exists=True))
@click.option('--insecure', is_flag=True)
@click.command()
def validate(connection_string, key_path):
    """
        Attempt to connect to a Shrub server and print a message
        detailing success or failure.
    """
    click.echo("Attempting to connect to '{}' with key '{}'".format(
               connection_string, key_path))

    connection_array = connection_string.split('@')
    if len(connection_array) == 2:
        username = connection_array[0]
        servername = connection_array[1]
    elif len(connection_array) == 1:
        username = getuser()
        servername = connection_array[0]
    else:
        click.echo("Error: Connection string should be in the format "
                   "'user@server'")
        return 1

    client = SSHClient()
    client.set_missing_host_key_policy(WarningPolicy())
    try:
        client.connect(username=username, hostname=servername,
                       key_filename=key_path)
    except PasswordRequiredException:
        prompt = 'Enter the password for key {}: '.format(key_path)
        password = getpass(prompt=prompt)
    try:
        client.connect(username=username, password=password,
                       hostname=servername, key_filename=key_path)
    except AuthenticationException:
        click.echo('Wrong password, exiting.')

    stdin, stdout, stderr = client.exec_command('ls -l')

    stdin, stdout, stderr = client.exec_command('shrubbery register
            {}'.format(username))

    output = stdout.read()
    client.close()

    if stdin or stdout or stderr:
        click.echo('Successfully connected, but Shrub does not give '
                   'interactive access.')

        # TODO: This is temp, remove soon.
        click.echo('P.S. output was\n\n: {}'.format(output))
        return 0
    else:
        click.echo('Error: could not connect')
        return 1

    return 1


def create_client(username, hostname, keyname):
    """Utility function to return an open SSHClient instance."""

cli.add_command(register)
cli.add_command(validate)
