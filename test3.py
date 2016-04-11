#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
#from textblob import TextBlob


con = None

try:
    con = lite.connect('tweeter.db')
    with con:
        array = []
        cur = con.cursor()    
	count = 0
        #for row in cur.execute("select word, count(*) from (select (case when instr(substr(Tweets2012.TweetText, nums.n+1), ' ') then substr(Tweets2012.TweetText, nums.n+1) else substr(Tweets2012.TweetText, nums.n+1, instr(substr(Tweets2012.TweetText, nums.n+1), ' ') - 1) end) as word from (select ' '||TweetText as TweetText from Tweets2012) Tweets2012 cross join (select 1 as n union all select 2 union all select 3 ) nums where substr(Tweets2012.TweetText, nums.n, 1) = ' ' and substr(Tweets2012.TweetText, nums.n, 1) <> ' ') w group by word order by count(*) desc"): 
       # for row in cur.execute("SELECT TweetText FROM Tweets2012 WHERE (Lower(TweetText) LIKE '%destroy%') AND (Lower(TweetText) LIKE '%obama%')"): 
	for row in cur.execute("SELECT * FROM Tweets2012"):
            count += 1
            array.append(row[0])
            print row[0]
        print count

    sentiments = []
    avg = 0

#    for tweet in array:
#
#        polarity = TextBlob(tweet).sentiment.polarity
#
#        sentiments.append(polarity)
#        avg += polarity
#
#    avg /= len(sentiments)
#    print avg
    
except lite.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
finally:
    
    if con:
        con.close()



