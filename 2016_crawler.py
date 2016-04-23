import sqlite3 as lite
import tweepy

consumer_key = "9Fdxn9FXXMwFurd7hC6dyM8xw"
consumer_secret = "XcRCSFsyOh536yaVixLJ0gboIKgk9JAi6JhYGZrvaLh4GbX1Cv"
access_token = "88537110-UsMFCkXU4wMcQPbamVaRaDMH94LejWTy6g4Ku2TC5"
access_token_secret = "B6AxbkZtFBKgpQlAPfxVUXXQXulhvt5L8bijvoe6WOoCi"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
class MyStreamListener(tweepy.StreamListener):
  def __init__(self, api=None):
    super(MyStreamListener, self).__init__()
    self.tweet_count = 0
    self.con = lite.connect('tweeter_2016.db')
    self.cur = self.con.cursor()
    self.cur.execute("CREATE TABLE IF NOT EXISTS Tweets2016(TweetId INT, TweetText TEXT)")

  def on_status(self, status):
      self.tweet_count += 1
      #print(status.id_str.encode("utf-8")+":"+status.text.encode("utf-8"))
      with self.con:
          self.cur.execute("INSERT INTO Tweets2016 VALUES(?,?)",(int(status.id_str.encode("utf-8")),status.text))
      if self.tweet_count % 500 == 0:
          print self.tweet_count;
      #print ""
      #if self.tweet_count <= 50:
      #  return True
      #else:
      #  return False

  def on_error(self, status_code):
      if status_code == 420:
          #returning False in on_data disconnects the stream
          return False


#con = None

#try:
#    con = lite.connect('tweeter_2016.db')
#    with con:
#        cur = con.cursor()
#	cur.execute("CREATE TABLE Tweets(TweetId INT, TweetText TEXT)")
#	cur.execute("INSERT INTO Tweets VALUES(2132313,'RT: FUCK YOU DONALD TRUMP')") 

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

myStream.filter(track=['Bernie','Sanders', 'bernie', 'sanders','Trump','trump'])

#print "New Filter:"
#myStreamListener = MyStreamListener()
#myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)

#myStream.filter(locations=[-86.33,41.63,-86.20,41.74])
