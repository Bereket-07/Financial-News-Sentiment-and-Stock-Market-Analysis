class FinancialAnalyzer:
    def __init__(self):
        pass

    def load_data(self, filepath):
        """Load stock data from a CSV file into a pandas DataFrame."""
        data = pd.read_csv(filepath, index_col='Date', parse_dates=True)
        return data

    def calculate_moving_average(self, data, window_size=20):
        """Calculate Simple Moving Average (SMA) using TA-Lib."""
        data['SMA'] = ta.SMA(data['Close'], timeperiod=window_size)
        return data

    def calculate_rsi(self, data, time_period=14):
        """Calculate Relative Strength Index (RSI) using TA-Lib."""
        data['RSI'] = ta.RSI(data['Close'], timeperiod=time_period)
        return data

    def calculate_ema(self, data, window_size=20):
        """Calculate Exponential Moving Average (EMA) using TA-Lib."""
        data['EMA'] = ta.EMA(data['Close'], timeperiod=window_size)
        return data

    def calculate_macd(self, data):
        """Calculate Moving Average Convergence Divergence (MACD) using TA-Lib."""
        data['MACD'], data['MACD_Signal'], _ = ta.MACD(data['Close'])
        return data

    def plot_data(self, data, y_columns, title):
        """Create a plot using Plotly."""
        self.fig = px.line(data, x=data.index, y=y_columns, title=title)
        self.fig.show()

    def analyze_stock(self, filename):
        """Perform the entire analysis on a single stock."""
        data = self.load_data(filename)
        
        # Calculate technical indicators
        data = self.calculate_moving_average(data)
        data = self.calculate_rsi(data)
        data = self.calculate_ema(data)
        data = self.calculate_macd(data)
        
        # Plot the results
        self.plot_data(data, ['Close', 'SMA'], 'Stock Price with Simple Moving Average (SMA)')
        self.plot_data(data, ['RSI'], 'Relative Strength Index (RSI)')
        self.plot_data(data, ['Close', 'EMA'], 'Stock Price with Exponential Moving Average (EMA)')
        self.plot_data(data, ['MACD', 'MACD_Signal'], 'Moving Average Convergence Divergence (MACD)')