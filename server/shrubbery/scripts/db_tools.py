#!/usr/bin/env python
from pysqlcipher3 import dbapi2 as sqlite
import bcrypt

PRAGMA = "PRAGMA key='FooBarBaz'"

# Inserts row in database, if username doesn't already exist
# Returns false if username exists
# Returns true if row was inserted
def insert_user_info_key(username, password, githubKey):
    if (username_exists(username)):
        return False
    
    sql = "INSERT INTO Users(username, passhash, github_key) VALUES ('{0}','{1}','{2}')".format(username, enc_pass(password), githubKey)

    # TODO: any other paths we should account for? unsure.
    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute(PRAGMA)
    c.execute(sql)

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
    
    sql = "INSERT INTO Users(username, passhash) VALUES ('{0}','{1}')".format(username, enc_pass(password))

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute(PRAGMA)
    c.execute(sql)

    conn.commit()
    conn.close()

    return True

# Updates the github key, given a valid username and password
# Returns false if the username doesn't exist
def change_githubKey(username, password, githubKey):
    if not (username_exists(username)):
        return False
    
    sql = "UPDATE Users Set github_key = '{0}' WHERE username = '{1}' and passhash = '{2}'".format(githubKey, username, enc_pass(password))
    
    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute(PRAGMA)
    c.execute(sql)

    conn.commit()
    conn.close()

    return True

# Gets the github key for a username and password
# Returns github key, or empty string if any error occurs
# Errors include: username doesn't exist, password doesn't match,
# no github key found
def retrieve_githubKey(username, password):
    if not (username_exists(username)):
        return ''
    if not (check_password(username, password)):
        return ''
    
    sql = "SELECT github_key FROM Users WHERE username = '{0}' and passhash = '{1}'"
        .format(username, enc_pass(password))

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute(PRAGMA)
    c.execute(sql)
    data=c.fetchall()
    conn.close()

    if len(data) != 1:
        return ''
    else:
        return data[0]


# Helper Methods

# Get encrypted password given plain password
def enc_pass(password):
    return bcrypt.hashpw(str.encode(password),bcrypt.gensalt(10))

# Return true if password and username match, otherwise false
def check_password(username, password):
    if not (username_exists(username)):
        return False

    sql = "SELECT username FROM Users WHERE username = '{0}' and passhash = '{1}'"
        .format(username, enc_pass(password))

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute(PRAGMA)
    c.execute(sql)
    data = c.fetchall()
    conn.close()

    if len(data) > 0:
        return True
    else:
        return False

# Returns true if username exists, otherwise false
def username_exists(username):
    sql = "SELECT username FROM Users WHERE username = '{0}'"
        .format(username)
    conn = sqlite.connect('shrub.db')
    c = conn.cursor()
    c.execute(PRAGMA)
    c.execute(sql)
    data = c.fetchall()
    conn.close()

    if len(data) > 0:
        return True
    else:
        return False


# Run Tests
def run_tests():
    print('Testing success cases')
    print(insert_user_info_key('tess1','pa$$','abc'))
    print(insert_user_info('tess2','o.o'))
    print((retrieve_githubKey('tess2','o.o') == ''))

    print(change_githubKey('tess1','pa$$','def'))
    print(change_githubKey('tess2','o.o','ghi'))

    print((retrieve_githubKey('tess1','pa$$') == 'def'))
    print((retrieve_githubKey('tess2','o.o') == 'ghi'))


    print('Testing fail cases')
    print(insert_user_info_key('tess1','anything','anything'))
    print(insert_user_info('tess2','anything'))
    print(change_githubKey('tess3','anything','anything'))
    print((not retrieve_githubKey('tess2','anything') == ''))
    print((not retrieve_githubKey('tess3','') == ''))

run_tests()