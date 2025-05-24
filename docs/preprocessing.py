import numpy as np
from sklearn.preprocessing import MinMaxScaler

def prepare_lstm_data(df, feature='Close', window_size=30):
    data = df[[feature]].values
    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(data)
    
    X, y = [], []
    for i in range(window_size, len(scaled_data)):
        X.append(scaled_data[i - window_size:i, 0])
        y.append(scaled_data[i, 0])
    
    return np.array(X), np.array(y), scaler
