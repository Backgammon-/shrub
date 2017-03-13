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

    ##### OVERRIDES #####
    def emptyline(self):
        # Follow shell behavior; do nothing and just print a new prompt.
        pass

    def default(self, line):
        print("""shrub: {}: command not found. Try "help".""".format(line.split(' ', 1)[0]))

    ##### COMMANDS #####
    def do_register(self, line):
        print("TODO: register")

    def do_login(self, line):
        """login [username]
        Authenticate yourself to Shrub. You will be prompted for your password."""
        password = getpass.getpass()
        print(password)
        pass

    def do_EOF(self, line):
        """Send EOF (Ctrl-D) to exit."""
        print("\nBye!")
        return True

    def do_test(self, line):
        """TODO: REMOVE"""
        send_server_cmd(line)

    def do_show_issues(self, line):
        print("TODO: show issues")

##### HELPERS #####
def send_server_cmd(command_string):
    """Execute a shrub command on the server and return stdout as a string."""
    client = open_ssh_client()
    stdin, stdout, stderr = client.exec_command("shrub" + command_string)
    #print(stdout.read().decode("utf-8"))
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
