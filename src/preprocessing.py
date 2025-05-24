
import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')
    df = df.dropna()
    return df
