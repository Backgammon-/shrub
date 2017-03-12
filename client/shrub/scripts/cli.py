"""The Shrub command-line interface."""


from getpass import getuser, getpass
from os.path import expanduser
from sys import exit

import click
from paramiko import (AuthenticationException, PasswordRequiredException, RSAKey,
                      SSHClient, WarningPolicy)


CONNECTION_STRING = 'shrub@104.236.0.123'


##### MAIN GROUP #######################################################
@click.group()
def cli():
    pass


##### REGISTER #########################################################
@click.argument('username')
@click.option('--key-path', default=expanduser('~/.ssh/id_rsa'),
              type=click.Path(exists=True))
@click.option('--insecure', is_flag=True)
@click.command()
def register(username, key_path, insecure):
    """Register a new GitHub user with the Shrub server."""

### Temporary section for telling the user what _should_ happen.
    if insecure:
        click.echo('Warning: using insecure code paths.')

    fingerprint = get_key_fingerprint(key_path)
    click.echo("This command should register a user with username '{}' "
               "and ssh key '{} using fingerprint '{}''".format(
                   username, key_path, fingerprint))

### Section for setting up the sever command string.
# This is a ripe place to open up user input vulnerabilities.
    options_string = ''
    if insecure:
        options_string += ' --insecure'
    command_string = 'shrubbery register {} {}'.format(fingerprint, username)
    command_string += options_string

### Section for opening up SSH connection.
    username, hostname = get_connection_tuple(CONNECTION_STRING)
    if not (username and hostname):
        exit('Bad connection string')
    client = open_ssh_client(username, hostname, key_path)

### Execute the command, and perform any back and forth logic necessary.
# Interactivity could be implemented at this point if necessary using
# by using multiple exec_command calls and asking for user input where
# necessary.
#
# stdin, stdout, and stderr are file-like objects, but are only
# readable while the client is open
    stdin, stdout, stderr = client.exec_command(command_string)

### Parse server output here.
    print('\n\nServer stdout:')
    for line in stdout:
        print(line)
    print('\n\nServer stderr:')
    for line in stderr:
        print(line)

### Close the connection.
# Make sure to do this, else Python might hang and leave your shell
# frozen.
    client.close()


##### VALIDATE #########################################################
@click.option('--key-path', default=expanduser('~/.ssh/id_rsa'),
              type=click.Path(exists=True))
@click.option('--insecure', is_flag=True)
@click.command()
def validate(key_path, insecure):
    """
        Attempt to connect to a Shrub server and print a message
        detailing success or failure.
    """
    if insecure:
        click.echo('Warning: using insecure code paths.')

    click.echo("Attempting to connect to '{}' with key '{}'".format(
               CONNECTION_STRING, key_path))

    username, hostname = get_connection_tuple(CONNECTION_STRING)
    if not (username and hostname):
        exit('Bad connection string')

    client = open_ssh_client(username, hostname, key_path)
    stdin, stdout, stderr = client.exec_command('ls -l')
    output = stdout.read()
    client.close()

    if stdin or stdout or stderr:
        click.echo('Successfully connected, but Shrub does not give '
                   'interactive access.')
        exit(0)
    else:
        exit('Failed to connect')
    exit(1)


##### SHOW GROUP #######################################################
@click.group()
def show():
    """List repositories, issues, pull requests, etc."""
    pass


@click.command()
def repos():
    """List all repos a user has."""
    click.echo('Listing repos.')


@click.command()
def issues():
    """List all issues in a repository."""
    click.echo('Listing issues.')


@click.command()
def comments():
    """List all comments on an issue or pull request."""
    click.echo('Showing comments.')


##### CREATE GROUP #######################################################
@click.group()
def create():
    """Create repositories, issues, pull requests, etc."""
    pass


@click.command()
def issue():
    """Create an issue."""
    click.echo('Creating an issue')


@click.command()
def comment():
    """Create a comment on an issue or pull request."""
    click.echo('Creating a comment.')


##### Utils ############################################################
def get_connection_tuple(connection_string):
    """
        Return the username and hostname from an arbitrary connection
        string. Returns None if the supplied string is invalid.
    """
    connection_array = connection_string.split('@')
    if len(connection_array) == 2:
        username = connection_array[0]
        servername = connection_array[1]
    elif len(connection_array) == 1:
        username = getuser()
        servername = connection_array[0]
    else:
        return (None, None)
    return (username, servername)


def open_ssh_client(username, servername, keypath):
    """Return an open paramiko.SSHClient instance."""
    client = SSHClient()
    client.set_missing_host_key_policy(WarningPolicy())
    try:
        client.connect(username=username, hostname=servername,
                       key_filename=keypath)
    except PasswordRequiredException:
        prompt = 'Enter the password for key {}: '.format(keypath)
        password = getpass(prompt=prompt)
        try:
            client.connect(username=username, password=password,
                           hostname=servername, key_filename=keypath)
        except AuthenticationException:
            exit('Failed to authenticate')
    return client


def get_key_fingerprint(keypath):
    """Return an SSH key fingerprint from its path."""
    try:
        key = RSAKey.from_private_key_file(keypath)
    except PasswordRequiredException:
        prompt = 'Enter the password for key {}: '.format(keypath)
        password = getpass(prompt=prompt)
        try:
            key = RSAKey.from_private_key_file(keypath, password=password)
        except AuthenticationException:
            exit('Failed to authenticate')
    return key.get_base64()


##### SETUP GROUPS #####################################################
show.add_command(repos)
show.add_command(issues)
show.add_command(comments)

create.add_command(issue)
create.add_command(comment)

cli.add_command(register)
cli.add_command(validate)
cli.add_command(show)
cli.add_command(create)
