import cmd
import getpass
import paramiko

CONNECTION_STRING = 'shrub@104.236.0.123'
SERVER_PASSWORD = 'swordfish'

class Shrub(cmd.Cmd):
    prompt = "shrub> "
    intro = """Welcome to shrub!\nTo get started, try "help".\n"""

    doc_header = "Available commands:"
    ruler = '-'

    user_creds = []

    ##### OVERRIDES #####
    def emptyline(self):
        # Follow shell behavior; do nothing and just print a new prompt.
        pass

    def default(self, line):
        print("""shrub: {}: command not found. Try "help".""".format(line.split(' ', 1)[0]))

    ##### COMMANDS #####
    def do_register(self, line):
        """register [username]
        Register for a new shrub account. The username should be your Github username.
        You will be prompted for your desired shrub password, then your Github password."""
        linesplit = line.split()
        if not len(linesplit) == 1:
            print("register: incorrect arguments; input only your username")
            return
        username = linesplit[0]

        response = send_server_cmd("check_username_exists {}".format(username))

        # TODO: Coordinate with server code
        if response == "taken":
            print("Sorry, that username's already taken.")
            return
        shrub_pass = getpass.getpass(prompt="New shrub password: ")
        github_pass = getpass.getpass(prompt="Github password: ")

        response = send_server_cmd("register {} {} {}".format(username, shrub_pass, github_pass))
        print(response)

    def do_login(self, line):
        """login [username]
        Authenticate yourself to Shrub. You will be prompted for your password."""
        if len(self.user_creds) <= 0:
            print("shrub: login: already logged in; restart shrub to login as a different user")
            return

        linesplit = line.split()
        if not len(linesplit) == 1:
            print("login: incorrect arguments; input only your username")
            return
        else:
            username = linesplit[0]

        password = getpass.getpass()

        # TODO: determine server reaction; basically check if username/pass is correct
        # if so, store username/pass in memory on client and keep sending it with future commands
        response = send_server_cmd("check_login {} {}".format(username, password))
        if response == "success":
            print("Success: now logged in as {}.".format(username))
            self.user_creds = [username, password]
        else:
            print("shrub: login: authentication failure")

    def do_EOF(self, line):
        """Send EOF (Ctrl-D) to exit."""
        print("\nBye!")
        return True

    def do_show_issues(self, line):
        print("TODO: show issues")

##### HELPERS #####
def send_server_cmd(command_string):
    """Execute a shrub command on the server and return stdout as a string."""
    client = open_ssh_client()
    stdin, stdout, stderr = client.exec_command("shrub " + command_string)
    return stdout.read().decode("utf-8")

def open_ssh_client():
    """Return an open paramiko.SSHClient instance."""
    (username, hostname) = get_connection_tuple(CONNECTION_STRING)
    client = paramiko.client.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(username=username, password=SERVER_PASSWORD, hostname=hostname)
    return client

def get_connection_tuple(connection_string):
    """
        Return the username and hostname from an arbitrary connection
        string. Returns None if the supplied string is invalid.
    """
    connection_array = connection_string.split('@')
    if len(connection_array) == 2:
        username = connection_array[0]
        servername = connection_array[1]
    else:
        return (None, None)
    return (username, servername)

if __name__ == '__main__':
    Shrub().cmdloop()
