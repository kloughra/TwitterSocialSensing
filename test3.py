#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from textblob import TextBlob


con = None

try:
    con = lite.connect('tweeter.db')
    with con:
        array = []
        cur = con.cursor()    
	count = 0
        for row in cur.execute("SELECT TweetText FROM Tweets2012 WHERE (Lower(TweetText) LIKE '%romney%') AND (Lower(TweetText) NOT LIKE '%obama%')"):
            count += 1
            array.append(row[0])
            print row[0]
        print count

    sentiments = []
    avg = 0

    for i in range(60,100):

        polarity = TextBlob(array[i]).sentiment.polarity

        sentiments.append(polarity)
        avg += polarity

    avg /= len(sentiments)
    print avg
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()



        
