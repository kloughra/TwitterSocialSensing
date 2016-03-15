#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('tweeter.db')
    with con:
        cur = con.cursor()    
        #cur.execute("CREATE TABLE Tweets(TweetId INT, TweetText TEXT)")
        #cur.execute("INSERT INTO Tweets VALUES(2132313,'RT: FUCK YOU DONALD TRUMP')") 
        #cur.execute("INSERT INTO Tweets VALUES(6772313,'Yay I love Bernie!')")
	count = 0
        #con.commit()
#        cur.execute('DELETE FROM Tweets2012 WHERE rowid NOT IN (SELECT MAX(rowid) FROM Tweets2012 GROUP BY TweetId)')
#        con.commit()
#        for row in cur.execute('SELECT TweetId, COUNT(*) c FROM Tweets2012 GROUP BY TweetId HAVING c > 1'):
        for row in cur.execute('SELECT * FROM Tweets2012'): #ORDER BY TweetId'):
#       #for row in cur.execute('SELECT TweetId FROM Tweets WHERE TweetText="Yay I love Bernie!" ORDER BY TweetId'):
            count += 1
#            print count
            print row
        print count
    #cur.execute('SELECT SQLITE_VERSION()')
    
    #data = cur.fetchone()
    
    #print "SQLite version: %s" % data                
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()



