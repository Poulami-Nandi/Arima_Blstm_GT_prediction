# Modeling Approach

## Problem Statement
We aim to forecast Apple’s stock closing prices by integrating traditional price indicators and behavioral data from Google Trends.

---

## Methodology

### 1. Data Cleaning
- Imputation of missing trend scores
- Alignment of OHLC and GT timeframes

### 2. ARIMA
- AIC-based model selection
- Residual diagnostic plots

### 3. BiLSTM
- Scaled time windows of 30 days
- Trend-enhanced input tensor

### 4. Comparison
- RMSE and MAE computed on test set
- Visual overlay of ARIMA vs BiLSTM predictions

---

## Observations

- BiLSTM captured turning points better
- ARIMA worked best for stationary residuals
- Google Trends had moderate predictive signal
