# Stock Trend Prediction using ARIMA, BiLSTM, and Google Trends

This project explores the combined use of traditional statistical models (ARIMA), deep learning (BiLSTM), and external search data (Google Trends) for predicting Apple Inc.'s stock price movements. The primary focus is to evaluate how combining time-series price data with behavioral indicators from Google Trends improves model performance.

---

## 📁 Project Structure
```bash
Arima_Blstm_GT_prediction/
├── data/
│ └── Apple_stock_GT_20200101_20250420.csv
├── notebooks/
│ └── Arima_Blstm_OHLC_GT.ipynb
├── src/
│ ├── data_loader.py
│ ├── preprocessing.py
│ └── model_utils.py
├── docs/
│ └── approach.md
├── README.md
└── requirements.txt
```

---

## 🔍 Key Features

- **ARIMA** for linear modeling of historical stock prices
- **BiLSTM** neural networks for capturing temporal patterns
- **Google Trends** integration as an external behavioral feature
- End-to-end data loading, preprocessing, training, and evaluation pipeline

---

## 🧪 Methods Used

### 1. **Exploratory Data Analysis**
- Correlation of stock OHLC and Google Trends keywords
- Rolling volatility and returns

### 2. **ARIMA Model**
- Trained on `Close` price
- Seasonal decomposition and parameter optimization

### 3. **BiLSTM**
- Scaled sequences of stock data + trend scores
- MSE and RMSE evaluation
- Comparison with ARIMA

---

## 📊 Data Sources

- Apple OHLCV data from Yahoo Finance
- Google Trends scores for selected search terms

---

## 🧠 Libraries Used

- pandas, numpy
- matplotlib, seaborn
- statsmodels
- tensorflow / keras
- sklearn
- pytrends

---

## 🗃️ File Descriptions

| File | Description |
|------|-------------|
| `data_loader.py` | Reads CSV and integrates Google Trends |
| `preprocessing.py` | Normalizes, sequences, and prepares inputs |
| `model_utils.py` | Builds and trains BiLSTM model |
| `Arima_Blstm_OHLC_GT.ipynb` | Full notebook with EDA and modeling |
| `approach.md` | Detailed technical write-up |

---

## 📌 How to Run

```bash
pip install -r requirements.txt
python -m src.data_loader
python -m src.preprocessing
python -m src.model_utils
```

Or use the Jupyter notebook directly.
---
## 📈 Results
- BiLSTM outperformed ARIMA on short-horizon prediction
- Google Trends features slightly improved early trend detection
- Integrated model reduced RMSE by ~10% compared to ARIMA-only baseline
---
## 📄 License    
This project is MIT licensed.  
---
## 🤝 Contributing    
Pull requests and issues are welcome!  
---
## 🔗 Author
Dr. Poulami Nandi  
📧 poulami.nandi91@gmail.com  
📘 Google Scholar  
🐙 GitHub  
