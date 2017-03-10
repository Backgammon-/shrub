from pysqlcipher3 import dbapi2 as sqlite

conn = sqlite.connect('shrub.db')
c = conn.cursor()
c.execute("PRAGMA key='FooBarBaz'")
c.execute("""CREATE TABLE Users(
    username TEXT NOT NULL,
    passhash TEXT NOT NULL,
    github_key TEXT,
    PRIMARY KEY(username)
    )""")

# e.g.:
# c.execute("INSERT INTO Users(username, passhash) VALUES ('John', '123456')")
# c.execute("INSERT INTO Users(username, passhash, github_key) VALUES ('Bob', '654321', 'foobarbaz')")
