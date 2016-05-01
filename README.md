# TwitterSocialSensing


Katie Loughran & Patrick Hansen
kloughra && phansen
CyberPhysical Systems and Social Sensing
Final Project
May 2nd 2016
Using Twitter Sentiment to Predict the Presidential Election


There are 6 files relevent to our project. They can be found in our github repository at this link:
https://github.com/kloughra/TwitterSocialSensing


The six files are the following:

===============
2016_crawler.py
===============
This file can be run by simply running it in python: 'python 2016_crawler.py'
This runs and pulls in tweets as they are tweeted if they contain the words hillary, clinton or trump. The results are put into a table in another file, tweeter_2016.db.

===============
tweeter_2016.db
===============
This file is a Sqlite database, and has two tables: Tweets2016_hillary and Tweets2016.
The former contains the tweets of Donald Trump and Hillary Clinton.
The latter contains the tweets of Donald Trump and Bernie Sanders.

===================
database_counter.py
===================
This is a file we used to count the numbers of tweets in the databases. It can really easily be modified to get information about the databases.

=============
statistics.py
============
This is the program we modified over to get different statistics on the data like polarity. It can be run with python 'python statistics.py'.

======================
tweet_id_crawler_db.py
======================
This is the program we used to get the tweets from the 2012 tweet ID database. It looks of tweets by arrays of id's 100 at a time.
This program can be run by tweet_id_crawler_db.py

==========
tweeter.db
=========
This is the sqlite database we used to store our Mitt Romney/Barack Obama tweets. The table in the database containing the tweets is called Tweets2012.

===========================================
election2012_tweetids_2012-07-01_2012-11-07
===========================================
This is a plain text file containling ~35 million tweet ids from the 2012 election.
