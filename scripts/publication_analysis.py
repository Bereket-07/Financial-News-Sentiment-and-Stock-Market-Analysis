class Publication_analysis:
    def __init__(self) -> None:
        pass
    def get_top_publihsers(self,top_what):
        # 1. Count the number of articles per publisher
        self.publisher_counts = df2['publisher'].value_counts()
        return self.publisher_counts.head(top_what)
    def analyze_the_sentiment_by_publisghers(self):
        # 2. Analyze the sentiment by publisher
        self.publisher_sentiment = df2.groupby('publisher')['nltk_sentiment'].mean()
        # Display the sentiment distribution for top publishers
        return self.publisher_sentiment
    def extract_domain(self,publisher):
        if '@' in publisher:
            return publisher.split('@')[-1]
        return publisher
    def extract_domains_from_email_addresses(self):
        try:
            self.df2['domain'] = df2['publisher'].apply(self.extract_domain)
            # Count the number of articles per domain
            self.domain_counts = df2['domain'].value_counts()
            return self.domain_counts
        except:
            return "no email address found"
    def plot_top_publishers(self,publisher_counts):
        # Top Publishers
        plt.figure(figsize=(10, 6))
        publisher_counts.head(10).plot(kind='bar', color='skyblue')
        plt.title('Top 10 Contributing Publishers')
        plt.xlabel('Publisher')
        plt.ylabel('Number of Articles')
        plt.xticks(rotation=45)
        plt.show()
    def plot_average_sentimetn_per_top_publishers(self, publisher_sentiment, publisher_counts):
        self.top_publishers = publisher_counts.index
        
        # Ensure that publisher_sentiment contains only the top publishers
        aligned_sentiment = publisher_sentiment.loc[self.top_publishers]
        
        # Plot
        plt.figure(figsize=(10, 6))
        aligned_sentiment.plot(kind='bar', color='orange')
        plt.title('Average Sentiment of Top 10 Publishers')
        plt.xlabel('Publisher')
        plt.ylabel('Average Sentiment Score')
        plt.xticks(rotation=45)
        plt.show()

    