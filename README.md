# Shrub -- A Command-Line Tool for Using GitHub

Shrub is a command-line client-server tool for using GitHub. It is being
developed as a final project for CS 377 (Software Security) at Drexel
University. The puprose is not so much to create a useful product as to
demonstrate some of the "sins" of software security and how they may be
mitigated.

This aplication is used from a client's computer to access various
GitHub API endpoints. Shrub uses a server application to actually
format these requests and handle authentication for the user, such that
a user who can SSH authenticate against the Shrub server will have their
GitHub credentials stored for them.

# Contents

    shrub/
    ├── README.md
    ├── client
    │   ├── shrub.py
    │   └── shrublib
    │       └── __init__.py
    └── server
        ├── shrubbery.py
            └── shrubberylib
                    └── __init__.py

                    4 directories, 5 files
