from textblob import TextBlob
from elasticsearch import Elasticsearch

es = Elasticsearch()



# pass tweet into TextBlob                                                        
tweets = ["good great wonderful awesome hi kt", "bad evil awful mitt romney hi kt"]
sentiments = []

for tweet in tweets:
    sentiments.append(TextBlob(tweet).sentiment.polarity)
    

print sentiments
