import tweepy
import csv
import json
import pandas as pd
import datetime
from datetime import date




CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)




with open('..\\shorttext\\twitter-train-full-A.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    i = 0
    for row in spamreader:
        i = i+1
        id =str(row[0])
        id = id.split(",")[0]
        try:
            data = api.get_status(id);
            with open("..\\shorttext\\downloads\\"+id+".json", 'w') as outfile:
                outfile.write(json.dumps(data._json))
                print(id)
        except:
                print("No status"+id)
                