import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import requests
import json
from blaze.server.serialization import json
from django.utils import encoding

########################################################################################################
########## I/P : Text to calculate its sentiment #######################################################
############ O/P : Calculating sentiment using NLTK library and sentiment140 ###########################
########################################################################################################



class Sentiment:
    def getSentimentNLTK(self,tweetSentence):
        score = []
               
        try:
            #print('==============getSentimentNLTK starts ====================')
            tweetSentence = encoding.smart_str(tweetSentence, encoding='ascii', errors='ignore')
            sid = SentimentIntensityAnalyzer()
            sentimentScore = sid.polarity_scores(tweetSentence)
            score.append(sentimentScore['neu']) 
            score.append(sentimentScore['neg']) 
            score.append(sentimentScore['pos']) 
            score.append(sentimentScore['compound']) 
        except :
            score = [0,0,0,0]

        return score    
    