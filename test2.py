from textblob import TextBlob
from elasticsearch import Elasticsearch

es = Elasticsearch()



# pass tweet into TextBlob                                                        
tweets = ["good great wonderful awesome hi kt", "bad evil awful mitt romney hi kt"]
sentiments = []
avg = 0

for tweet in tweets:
    
    polarity = TextBlob(tweet).sentiment.polarity

    sentiments.append(polarity)
    avg += polarity

avg /= len(sentiments)
