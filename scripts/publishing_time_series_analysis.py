import  matplotlib.pyplot as plt

class Publishing_time_series_Analysis:
    def __init__(self) -> None:
        pass
    def preprocess_for_hourly(self,data):
        data['hour'] = data.index.hour
        self.hourly_distribution = data.groupby('hour').size()
        return self.hourly_distribution
    def preprocess_for_minuitly(self,data):
        data['minute'] = data.index.minute
        self.minutly_distribution = data.groupby('minute').size()
        return self.minutly_distribution
    def plot_time_series(self,data_to_analyze):
        # Plot the distribution of news publishing times by hour

        plt.figure(figsize=(14, 8))  # Increase figure size for better visibility
        data_to_analyze.plot(kind='bar', color='skyblue')
        plt.title('Distribution of News Publishing Times by Hour')
        plt.xlabel('Minutes/Hours of the Day')
        plt.ylabel('Number of News Items')
        plt.xticks(rotation=45, fontsize=8)  # Rotate labels and increase font size
        plt.grid(True)
        plt.show()
