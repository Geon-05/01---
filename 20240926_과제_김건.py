import pandas as pd

class Outlier:
    def __init__(self, df, col):
        self.df = df
        self.col = col
        
        self.mn, self.c, self.mx = df[col].quantile([0.25,0.5,0.75])
        # self.mn = mn
        # self.c = c
        # self.mx = mx
        
        self.IQR = self.mx - self.mn
    
    def max_outlier(self):
        max_ol = self.mx + (self.IQR * 1.5)
        res_df = self.df[self.df[self.col] > max_ol].reset_index(drop=True)
        return res_df
    
    def min_outlier(self):
        min_ol = self.mn - (self.IQR * 1.5)
        res_df = self.df[self.df[self.col] < min_ol].reset_index(drop=True)
        return res_df
    
    def normaldf(self):
        con1 = self.df[self.col] <= self.mx + (self.IQR * 1.5)
        con2 = self.df[self.col] >= self.mn - (self.IQR * 1.5)
        res_df = self.df[con1 & con2].reset_index(drop=True)
        return res_df
    
if __name__=='__main__':
    df = pd.read_csv('./data/house_price_clean.csv')
    
    test = Outlier(df,"분양가")
    print(test.max_outlier())
    print(test.min_outlier())
    print(test.normaldf())