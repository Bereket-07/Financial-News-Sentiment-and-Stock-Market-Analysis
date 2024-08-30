class check_data_before_analysis:
    def __init__(self):
        pass
    def load_stock_data(self,filepath):
        self.data = pd.read_csv(filepath)
        return self.data.head()
    