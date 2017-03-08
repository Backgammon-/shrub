# Shrub Client Application

The Shrub Client Application is provided as a package with a setup
script to create the `shrub` command-line application.

It is best used and developed on with a Python Virtual Environment. To
build and install the Shrub, do the following:

1. Install `virtualenv` on your platform.
2. Create a Python 3 virtual environment (preferably in the root of this
   repository) using the command `virtualenv -p python3 venv`
3. Activate that virtual environment using `source venv/bin/activate`
4. Copy the Shrub setup script to your current working directory 
   via `cp client/shrub/scripts/setup.py .` or symlink it using `ln -s
   client/shrub/scripts/setup.py`
5. Install the module using `pip install --editable .`

You will need to run the `pip install --editable .` command everytime
you make changes to any of the files in the package.

Once you have installed the package, the `shrub` command should be
available in your console.
