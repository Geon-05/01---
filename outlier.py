import pandas as pd

def iqr(df,col):
    mn, c, mx = df[col].quantile([0.25,0.5,0.75])
    IQR = mx - mn
    return mn,c,mx,IQR

def max_outlier(df,col):
    _,_,mx,IQR = iqr(df,col)
    max_ol = mx + (IQR * 1.5)
    res_df = df[df[col]>max_ol].reset_index(drop=True)
    return res_df

def min_outlier(df,col):
    mn,_,_,IQR = iqr(df,col)
    min_ol = mn - (IQR * 1.5)
    res_df = df[df[col]<min_ol].reset_index(drop=True)
    return res_df

def normaldf(df,col):
    mn,_,mx,IQR = iqr(df,col)
    con1 = df[col] <= mx + (IQR * 1.5)
    con2 = df[col] >= mn - (IQR * 1.5)
    res_df = df[con1 & con2].reset_index(drop=True)
    return res_df

if __name__=='__main__':
    df = pd.read_csv('./data/house_price_clean.csv')
    max_ol_df = max_outlier(df,'분양가')
    print(max_ol_df)
    
    print("="*30)
    
    min_ol_df = min_outlier(df,'분양가')
    print(min_ol_df)
    
    print("="*30)
    
    normal = normaldf(df,'분양가')
    print(normal)