#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys

con = None

try:
    con = lite.connect('tweeter_2016.db')
    with con:
        array = []
        cur = con.cursor()    
	count = 0
        for row in cur.execute("SELECT TweetText FROM Tweets2016_hillary"):
            count += 1
        print count
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()



        
