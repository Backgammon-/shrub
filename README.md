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

# Setup and Development

Shrub is best used on Linux, but the client package can also be
installed on macOS and Windows relativeley easily.

Development is best done in a virtual environment, so you will first
need to install virtualenv on your platform. You can use a single
virtual environment to develop on both the shrub (client) package and
the shrubbery (server) package simultaneously.

* Create, activate, and verify your virtual environment in the root of
  the repository:

```
shrub/ $ virtualenv venv --python=python3
shrub/ $ source venv/bin/activate
(venv) shrub/ $ python --version   # should print out your python3 version
```

* Now you can use pip to install the two packages in your virtual
  environment.

```
(venv) shrub/ $ pip install client --editable
(venv) shrub/ $ pip install server --editable
```

* This will make available the `shrub` and `shrubbery` executables
  which can be called as a bare command like any other program:

```
(venv) shrub/ $ shrub --help
(venv) shurb/ $ shrubbery --help
```

* When you make a change to these packages, you must rerun the above
  `pip` commands for them to propagate to the 

# Dependencies

The shrub server uses SQLite and SQLCipher, both of which must be
installed on an OS level before the package can be built. These are
nontrivial to install on Windows/macOS, so it is best to use Linux
instead.
