#!/usr/bin/env python
from pysqlcipher3 import dbapi2 as sqlite
import bcrypt

PRAGMA = "PRAGMA key='FooBarBaz'"

# Inserts row in database, if username doesn't already exist
# Returns false if username exists
# Returns true if row was inserted
def insert_user_info_key(username, password, githubKey, insecure=False):
    if (username_exists(username)):
        return False

    # TODO: any other paths we should account for? unsure.
    conn = sqlite.connect('shrub.db')
    c = conn.cursor()

    if insecure:
        sql = ("INSERT INTO Users(username, passhash, github_key) "
               "VALUES ('{}','{}','{}')".format(username,
                                                enc_pass(password),
                                                githubKey))
        compound_sql = PRAGMA + '; ' + sql
        c.executescript(compound_sql)
    else:
        sql = ("INSERT INTO Users(username, passhash, github_key) "
               "VALUES (:username, :passhash, :github_key)")
        c.execute(PRAGMA)
        c.execute(sql, {"username": username,
                        "passhash": enc_pass(password),
                        "github_key": githubKey})

    conn.commit()
    conn.close()

    return True

# Inserts row in database, if username doesn't already exist
# Does not add github key to row, so that column will be blank
# Returns false if username exists
# Returns true if row was inserted
def insert_user_info(username, password, insecure=False):
    if (username_exists(username)):
        return False

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()

    if insecure:
        sql = ("INSERT INTO Users(username, passhash) "
               "VALUES ('{}','{}')".format(username, enc_pass(password)))
        compound_sql = PRAGMA + '; ' + sql
        c.executescript(compound_sql)
    else:
        sql = ("INSERT INTO Users(username, passhash) "
               "VALUES (:username, :passhash)")
        c.execute(PRAGMA)
        c.execute(sql, {"username": username,
                        "passhash": enc_pass(password)})

    conn.commit()
    conn.close()

    return True

# Updates the github key, given a valid username and password
# Returns false if the username doesn't exist
#def change_githubKey(username, password, githubKey):
#    if not (username_exists(username)):
#        return False

#    # TODO: if we end up using this function, MUST add password verification
#
#    sql = "UPDATE Users Set github_key = '{}' WHERE username = '{}'".format(githubKey, username)

#    conn = sqlite.connect('shrub.db')
#    c = conn.cursor()
#    c.execute(PRAGMA)
#    c.execute(sql)

#    conn.commit()
#    conn.close()

#    return True

# Gets the github key for a username and password
# Returns github key, or empty string if any error occurs
# Errors include: username doesn't exist, password doesn't match,
# no github key found
def retrieve_githubKey(username, password, insecure=False):
    if not (username_exists(username)):
        return ''
    if not (check_password(username, password)):
        return ''

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()

    if insecure:
        sql = ("SELECT passhash, github_key FROM Users "
               "WHERE username = '{}'".format(username))
        compound_sql = PRAGMA + '; ' + sql
        c.executescript(compound_sql)
    else:
        sql = ("SELECT passhash, github_key FROM Users "
               "WHERE username = :username")
        c.execute(PRAGMA)
        c.execute(sql, {"username": username})

    data=c.fetchall()
    conn.close()

    if len(data) == 1 and len(data[0]) > 1 and not(data[0][1] == None) and compare_crypt(data[0][0],password):
        return data[0][1]
    else:
        return ''

# Helper Methods

# Get encrypted password given plain password
def enc_pass(password):
    return bcrypt.hashpw(password.encode('ascii'),bcrypt.gensalt(10)).decode('ascii')

# Compares hashed string with unencrypted string
# Returns true if equal
# False otherwise
def compare_crypt(plainhash, plaintext):
    hash = plainhash.encode('ascii')
    text = plaintext.encode('ascii')
    return bcrypt.checkpw(text, hash)

# Return true if password and username match, otherwise false
def check_password(username, password, insecure=False):
    if not (username_exists(username)):
        return False

    conn = sqlite.connect('shrub.db')
    c = conn.cursor()

    if insecure:
        sql = "SELECT passhash FROM Users WHERE username = '{}'".format(username)
        compound_sql = PRAGMA + '; ' + sql
        c.executescript(compound_sql)
    else:
        sql = "SELECT passhash FROM Users WHERE username = :passhash"
        c.execute(PRAGMA)
        c.execute(sql, {"passhash": passhash})

    data = c.fetchall()
    conn.close()

    if len(data) > 0 and len(data[0]) > 0 and compare_crypt(data[0][0],password):
        return True
    else:
        return False

# Returns true if username exists, otherwise false
def username_exists(username, insecure=False):
    conn = sqlite.connect('shrub.db')
    c = conn.cursor()

    if insecure:
        sql = "SELECT username FROM Users WHERE username = '{}'".format(username)
        compound_sql = PRAGMA + '; ' + sql
        c.executescript(compound_sql)
    else:
        sql = "SELECT username FROM Users WHERE username = :username"
        c.execute(PRAGMA)
        c.execute(sql, {"username": username})

    data = c.fetchall()
    conn.close()

    if len(data) > 0:
        return True
    else:
        return False

# Run Tests
def run_tests():
    print('Testing success cases')
    print(compare_crypt(enc_pass('pass'),'pass'))

    print(insert_user_info_key('tess1','pa$$','abc'))
    print(insert_user_info('tess2','o.o'))

    print((retrieve_githubKey('tess1','pa$$') == 'abc'))
    print((retrieve_githubKey('tess2','o.o') == ''))

    print('Testing fail cases')
    print(insert_user_info_key('tess1','anything','anything'))
    print(insert_user_info('tess2','anything'))
    print((not retrieve_githubKey('tess1','anything') == ''))
    print((not retrieve_githubKey('tess2','anything') == ''))

#run_tests()
