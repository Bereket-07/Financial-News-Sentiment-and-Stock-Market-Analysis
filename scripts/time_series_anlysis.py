from statsmodels.tsa.seasonal import seasonal_decompose


class Time_series_analysis:
    def __init__(self) -> None:
        pass
    def time_stamp_by_year(self,rank):
        # Resample data by year and count headlines
        self.resamble_data_by_year = df2['headline'].resample('YE').count()
        self.top_five_years = self.resamble_data_by_year.sort_values(ascending=False).head(5)
        self.first_best = self.top_five_years.index[rank]

        # Filter data for the selected year
        self.data_top_year = df2[df2.index.year == self.first_best.year]
        
        # Group by date (self.data_top_year.index) to count daily headlines
        self.daily_headlines = self.data_top_year.groupby(self.data_top_year.index).size()
        
        # Create a DataFrame for the time series
        self.time_series_data_of_headline_count = pd.DataFrame({'Headlines_Count': self.daily_headlines})
        return self.time_series_data_of_headline_count

    def plot_time_series(self,time_series_data_of_headline_count):

        decomposition = seasonal_decompose(time_series_data_of_headline_count['Headlines_Count'], model='additive', period=30)

        plt.figure(figsize=(14, 10))

        plt.subplot(411)
        plt.plot(time_series_data_of_headline_count['Headlines_Count'], label='Original', color='blue')
        plt.legend(loc='upper left')

        plt.subplot(412)
        plt.plot(decomposition.trend, label='Trend', color='orange')
        plt.legend(loc='upper left')

        plt.subplot(413)
        plt.plot(decomposition.seasonal, label='Seasonal', color='green')
        plt.legend(loc='upper left')

        plt.subplot(414)
        plt.plot(decomposition.resid, label='Residual/Irregular', color='red')
        plt.legend(loc='upper left')

    plt.tight_layout()
    plt.show()
