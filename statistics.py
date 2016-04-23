#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
from textblob import TextBlob


con = None

try:
    con = lite.connect('tweeter_2016.db')
    with con:
        array = []
        cur = con.cursor()    
	count = 0
        for row in cur.execute("SELECT TweetText FROM Tweets2016_hillary WHERE (Lower(TweetText) LIKE '%trump%') AND ((Lower(TweetText) NOT LIKE '%hillary%') AND (Lower(TweetText) NOT LIKE '%clinton%'))"):
            count += 1
            array.append(row[0])
            #print row[0]
        print count

    sentiments = []
    subjects = []
    avg = 0
    savg = 0
    countp = 0
    countn = 0
    countt = 0

    for i in range(len(array)):

        polarity = TextBlob(array[i]).sentiment.polarity
        sub = TextBlob(array[i]).sentiment.subjectivity

        if polarity > 0:
            countp += 1
        elif polarity < 0:
            countn += 1
        else:
            countt += 1

        subjects.append(sub)
        sentiments.append(polarity)
        avg += polarity
        savg += sub

    avg /= len(sentiments)
    savg /= len(subjects)
    print 'avg sentiment: ', avg
    print 'avg subjectiv: ', savg
    print 'positive coun: ', countp
    print 'negative coun: ', countn
    print 'zero count   : ', countt
    
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()



        
