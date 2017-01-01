import sqlite3

with sqlite3.connect("blog.db") as connection:
    c = connection.cursor()
    #create posts table
    '''c.execute(""" CREATE TABLE posts
            (title TEXT, post TEXT)
              """)'''
    #populate the table with dummy posts
    c.execute('INSERT INTO posts VALUES("Good", "I\'m feeling good")')
    c.execute('INSERT INTO posts VALUES("Shit", "I\'m like shit")')
    c.execute('INSERT INTO posts VALUES("Soso", "I\'m not feeling very good")')
    c.execute('INSERT INTO posts VALUES("Super", "I\'m superduper dude!")')
    c.execute('INSERT INTO posts VALUES("Merda", "I\'m sentirmi di merda")')
