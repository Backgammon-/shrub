import cmd
import getpass

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

    def do_show_issues(self, line):
        print("TODO: show issues")

    ##### HELPERS #####
    def send_server_cmd():
        # TODO: Use Paramiko to execute a command on the server and return the server's response.
        pass

if __name__ == '__main__':
    Shrub().cmdloop()
