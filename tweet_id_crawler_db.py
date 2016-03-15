import sqlite3 as lite
import sys

import tweepy

consumer_key = "9Fdxn9FXXMwFurd7hC6dyM8xw"
consumer_secret = "XcRCSFsyOh536yaVixLJ0gboIKgk9JAi6JhYGZrvaLh4GbX1Cv"
access_token = "88537110-UsMFCkXU4wMcQPbamVaRaDMH94LejWTy6g4Ku2TC5"
access_token_secret = "B6AxbkZtFBKgpQlAPfxVUXXQXulhvt5L8bijvoe6WOoCi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


con = None

try:
    con = lite.connect('tweeter.db')


    with open("election2012_tweetids_2012-07-01_2012-11-07") as myfile:
        tweet_ids = [next(myfile) for x in xrange(45000)]
    print "Got Tweet ids"
    for tid in tweet_ids:
        i = tweet_ids.index(tid)
        tweet_ids[i]=tid.split('\r\n')[0]
	count = 0
        r1 = 25000#16199 #10000
        r2 = 25099
        #total_tweets = []
    print "Ready to get tweets"
    with con:

        cur = con.cursor()
#        cur.execute("CREATE TABLE Tweets2012(TweetId INT, TweetText TEXT)")
        bbcount = 0
        while count<20000:
            tweets = api.statuses_lookup(id_=tweet_ids[r1:r2], include_entities = True)
            for tweet in tweets:
                bbcount += 1
                print bbcount
#                print tweet.text.encode("utf-8").replace("\"","")
                cur.execute("INSERT INTO Tweets2012 VALUES(?,?)",(int(tweet.id_str.encode("utf-8")),tweet.text))#% (int(tweet.id_str.encode("utf-8")), tweet.text.encode("utf-8").replace("\"","\\\"")))
#            total_tweets.extend(tweets)
            r1 += 100
            r2 += 100
            count += 100
            con.commit()
#        for row in cur.execute('SELECT TweetId FROM Tweets WHERE TweetText="Yay I love Bernie!" ORDER BY TweetId'):
#            print row


    #data = cur.fetchone()
    #print "SQLite version: %s" % data                

except lite.Error, e:

    print "Error %s:" % e.args[0]
    sys.exit(1)

finally:

    if con:
        con.close()





