# Stock Trend Prediction with ARIMA & BLSTM using OHLC + Google Trends Data

This project demonstrates how to forecast Apple Inc. stock prices by leveraging both financial OHLC data and public sentiment data obtained from Google Trends.

## Components

- `notebooks/Arima_Blstm_OHLC_GT.ipynb`: Main notebook with ARIMA and BLSTM models.
- `data/Apple_stock_GT_20200101_20250420.csv`: Pre-collected Google Trends data for "Apple stock".
- `src/`: Folder for Python modules (future improvements).
- `docs/`: Documentation and diagrams (future improvements).

## Features

- Google Trends integration with caching.
- Time-series modeling using:
  - ARIMA (for statistical baselines)
  - Bi-directional LSTM (for deep learning forecasts)
- Combined dataset creation for modeling.

## Getting Started

To use this project:
1. Clone the repo.
2. Open the notebook inside the `notebooks/` folder.
3. Ensure dependencies are installed (`requirements.txt`).

## Requirements

```bash
pip install -r requirements.txt
```

## Author

Dr. Poulami Nandi
