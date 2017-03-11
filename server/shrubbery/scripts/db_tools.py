#!/usr/bin/env python
from pysqlcipher3 import dbapi2 as sqlite
import bcrypt

# Inserts row in database, if username doesn't already exist
# Returns false if username exists
# Returns true if row was inserted
def insert_user_info(username, password, githubKey):
    if (username_exists(username)):
        return False

    # TODO: any other paths we should account for? unsure.
    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute("PRAGMA key='FooBarBaz'")
    c.execute("INSERT INTO Users(username, passhash, github_key) " +
        "VALUES ('%s','%s','%s')".format(
            username, enc_pass(password), githubKey))

    conn.commit()
    conn.close()

    return True

# Inserts row in database, if username doesn't already exist
# Does not add github key to row, so that column will be blank
# Returns false if username exists
# Returns true if row was inserted
def insert_user_info(username, password):
    if (username_exists(username)):
        return False

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute("PRAGMA key='FooBarBaz'")
    c.execute("INSERT INTO Users(username, passhash) " +
        "VALUES ('%s','%s')".format(username, enc_pass(password)))

    conn.commit()
    conn.close()

    return True

# Updates the github key, given a valid username and password
# Returns false if the username doesn't exist 
def change_githubKey(username, password, githubKey):
    if not (username_exists(username)):
        return False

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute("PRAGMA key='FooBarBaz'")
    c.execute("UPDATE Users Set github_key = '%s' "
        "WHERE username = '%s' and passhash = '%s'".format(
            githubKey, username, enc_pass(password)))

    conn.commit()
    conn.close()

    return True

# Gets the github key for a username and password
# Returns github key, or empty string if any error occurs
# Errors include: username doesn't exist, password doesn't match, no github key found
def retrieve_githubKey(username, password):
    if not (username_exists(username)):
        return ''
    if not (check_password(username, password)):
        return ''

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute("PRAGMA key='FooBarBaz'")
    c.execute(
        "SELECT github_key FROM Users WHERE username = '%s' and passhash = '%s'"
        .format(username, enc_pass(password)))
    data=cursor.fetchall()
    conn.close()

    if len(data) != 1:
        return ''
    else:
        return data[0]


# Helper Methods

# Get encrypted password given plain password
def enc_pass(password):
    return bcrypt.hashpw(password,bcrypt.gensalt())

# Return true if password and username match, otherwise false
def check_password(username, password):
    if not (username_exists(username)):
        return False

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute("PRAGMA key='FooBarBaz'")
    c.execute("SELECT username FROM Users WHERE username = '%s' and passhash = '%s'".format(username, enc_pass(password)))
    data = cursor.fetchall()
    conn.close()

    if len(data) > 0:
        return True
    else:
        return False

# Returns true if username exists, otherwise false
def username_exists(username):
    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute("PRAGMA key='FooBarBaz'")
    c.execute("SELECT username FROM Users WHERE username = '%s'".format(username))
    data = cursor.fetchall()
    conn.close()

    if len(data) > 0:
        return True
    else:
        return False
