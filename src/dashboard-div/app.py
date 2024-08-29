







import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

class StockMarketNewSentiment:
    def __init__(self,data):
        self.data = data
    def load_data(self,filepath):
        # loading the data
        self.data = pd.read_csv(filepath)
        return self.data
    def preprocess_text(self,text_column):
        #preprocess text data: remove NaN . lowercase, etc 
        self.data[text_column] = self.data[text_column].dropna().apply(lambda x : x.lower)
        return self.data[text_column]
    
    def analyze_sentiment(self,text_column):
        # perform sentiment analysis on the text column
        self.data['sentiment'] = self.data[text_column].apply(lambda x: TextxBlob(x).sentiment.polarity)
        return self.data['sentiment']
    def classify_sentiment(self):
        # classisfy sentiment as 1 (positive), 0 (neutral) , or -1(negative)
        self.data['sentiment_Label'] = self.data['sentiment'].apply(
            lambda x: 1 if x > 0 else (-1 if x < 0 else 0)
        )
        return self.data[['sentiment' , 'sentiment_Label']]
    def get_summery(self):
        # get a summery of sentiment Counts
        summery = self.data['sentiment_Label'].value_counts()
        return summery