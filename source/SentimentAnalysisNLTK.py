import pandas as pd
import os
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from Sentiment import Sentiment
import re
from SvmClassification import SvmClassification 
from django.utils import encoding

class SentimentAnalysisNLTK:
    
    def __init__(self):    
        self.positive = list()
        self.negative = list()
        self.neutral =  list()
        self.compound = list()
        self.type = list()
        self.text = list()
        self.score = list()
        self.originalScore = list()
        self.calculatedScore = list()
        
    def getSentiments(self,path):
        dirs = os.listdir( path )
        for file in dirs:
            formatedText = list()
            filename = path+file
            df = pd.read_csv(filename)
            self.type = df[['0']]
            type = self.type.values.tolist() 
            self.text = df[['1']]
            text = self.text.values.tolist() 
            self.originalScore = df [['2']]
            originalScore = self.originalScore.values.tolist() 
        
                    
            for i in range(len(text)):
                findSentimentText = text[i]
                findSentimentText = encoding.smart_str(findSentimentText, encoding='ascii', errors='ignore')
                
                findSentimentText = findSentimentText.lower()
                findSentimentText = re.sub('((www\.[^\s]+)|(https?://[^\s]+))','URL',findSentimentText)
                findSentimentText = re.sub('@[^\s]+','AT_USER',findSentimentText)
                findSentimentText = re.sub('[\s]+', ' ', findSentimentText)
                findSentimentText = re.sub(r'#([^\s]+)', r'\1', findSentimentText)
                findSentimentText = findSentimentText.strip('\'"')
                findSentimentText = re.sub('\\\[^\s]+','special_symbol',findSentimentText)
                
                formatedText.append(findSentimentText)
                
               
            
                

        
path = "..\\shorttext\\labled\\marged\\"
sentiAnalysis = SentimentAnalysisNLTK()
sentiAnalysis.getSentiments(path)  