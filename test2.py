from textblob import TextBlob
from elasticsearch import Elasticsearch

es = Elasticsearch()



# pass tweet into TextBlob                                                        
tweets = ["Sununu: Obama campaign definitely behind Reids outlandish accusation"]
sentiments = []
avg = 0

for tweet in tweets:
    
    polarity = TextBlob(tweet).sentiment.polarity

    sentiments.append(polarity)
    avg += polarity

print sentiments
avg /= len(sentiments)
