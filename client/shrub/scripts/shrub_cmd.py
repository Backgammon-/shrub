import cmd
import getpass

class Shrub(cmd.Cmd):
    prompt = "shrub> "
    intro = "Welcome to Shrub!"

    doc_header = "Available commands:"
    ruler = '-'

    def do_login(self, line):
        """login [username]
        Authenticate yourself to Shrub. You will be prompted for your password."""
        password = getpass.getpass()
        print(password)
        pass

    def do_EOF(self, line):
        print("\nBye!")
        return True

if __name__ == '__main__':
    Shrub().cmdloop()
