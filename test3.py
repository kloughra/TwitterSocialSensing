#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('tweeter.db')
    with con:
        array = []
        cur = con.cursor()    
	count = 0
        for row in cur.execute('SELECT TweetText FROM Tweets2012'): #ORDER BY TweetId'):
#       #for row in cur.execute('SELECT TweetId FROM Tweets WHERE TweetText="Yay I love Bernie!" ORDER BY TweetId'):
            count += 1
            array.append(row[0])
#            print count
            print row[0]
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



