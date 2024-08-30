from nltk.sentiment import SentimentIntensityAnalyzer
import pandas as pd

class NltkSentiment:
    def __init__(self, location):
        self.sia = SentimentIntensityAnalyzer()
        self.location = location
        self.data = None  # Initialize self.data to None

    def check(self):
        return f'It is working {self.location}'

    def load_data(self):
        # Loading the data
        self.data = pd.read_csv(self.location)
        return self.data

    def preprocess_text(self, text_column):
        # Preprocess text data: remove NaN, lowercase, etc.
        self.data[text_column] = self.data[text_column].dropna().apply(lambda x: x.lower())
        return self.data[text_column]

    def analyze_sentiment(self, text_column):
        # Perform sentiment analysis on the text column
        self.data['sentiment_nltk'] = self.data[text_column].apply(lambda x: self.sia.polarity_scores(x)['compound'])
        return self.data['sentiment_nltk']

    def classify_sentiment(self):
        # Classify sentiment as 1 (positive), 0 (neutral), or -1 (negative)
        self.data['sentiment_Label'] = self.data['sentiment_nltk'].apply(
            lambda x: 1 if x > 0 else (-1 if x < 0 else 0)
        )
        return self.data[['sentiment_nltk', 'sentiment_Label']]

    def get_summary(self):
        # Get a summary of sentiment counts
        summary = self.data['sentiment_Label'].value_counts()
        return summary