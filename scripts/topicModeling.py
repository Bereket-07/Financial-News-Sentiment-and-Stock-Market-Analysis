from nltk.corpus import stopwords
import nltk
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures
import string

class Identifing_commen_words():
    def __init__(self, data):
        self.data = data
        # Download NLTK data files (only need to do this once)
        import nltk
        nltk.download('punkt')
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
        self.punctuation = string.punctuation
    
    def add_to_lsit(self):
        self.headline = self.data['headline'].dropna().tolist()
        return self.headline
    
    def text_cleaning_process(self, text):
        self.tokens = word_tokenize(text.lower())  # Convert to lowercase and tokenize
        self.tokens = [word for word in self.tokens if word.isalpha()]  # Remove punctuation
        self.tokens = [word for word in self.tokens if word not in self.stop_words]  # Remove stop words
        return self.tokens
    
    def clean_data(self, headline):
        self.cleand_headlines = [self.text_cleaning_process(head) for head in headline]
        return self.cleand_headlines
    
    def tokenize_and_frequency_distribution(self,cleand_headlines):
        self.all_words = [word for token in cleand_headlines for word in token]
        return self.all_words
    
    def the_most_frequnent(self,all_words):
        self.most_frequent = FreqDist(all_words)
        return self.most_frequent.most_common()
    
    def bigram_analysis(self, all_words,num ):
        self.bigram_finder = BigramCollocationFinder.from_words(all_words)
        self.bigrams = self.bigram_finder.nbest(BigramAssocMeasures.likelihood_ratio, num)
        return self.bigrams
    
    def trigram_analysis(self, all_words,num):
        self.trigram_finder = TrigramCollocationFinder.from_words(all_words)
        self.trigrams = self.trigram_finder.nbest(TrigramAssocMeasures.likelihood_ratio, num)
        return self.trigrams
