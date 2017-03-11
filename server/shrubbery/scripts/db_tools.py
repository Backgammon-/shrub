#!/usr/bin/env python
from pysqlcipher3 import dbapi2 as sqlite
import bcrypt

def insert_user_info(username, password, githubKey):
    if (username_exists(username)):
        return False

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute("PRAGMA key='FooBarBaz'")
    c.execute("INSERT INTO Users(username, passhash, github_key) " +
        "VALUES ('%s','%s','%s')".format(username, enc_pass(password), githubKey))

    conn.commit()
    conn.close()

    return True

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

# Returns github key, or empty string if any error occurs
def retrieve_githubKey(username, password):
    if not (username_exists(username)):
        return ''
    if not (check_password(username, password)):
        return ''

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute("PRAGMA key='FooBarBaz'")
    c.execute("SELECT github_key FROM Users WHERE username = '%s' and passhash = '%s'"
        .format(username, enc_pass(password)))
    data=cursor.fetchall()
    conn.close()

    if len(data) != 1:
        return ''
    else:
        return data[0]


# Helper Methods

# Get encrypted password
def enc_pass(password):
    return bcrypt.hashpw(password,bcrypt.gensalt())

# Return true if password and username match, otherwise false
def check_password(username, password):
    if not (username_exists(username)):
        return False

    enc_pass = sha1(password)

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute("PRAGMA key='FooBarBaz'")
    c.execute("SELECT username FROM Users WHERE username = '%s' and passhash = '%s'".format(username, enc_pass))
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
