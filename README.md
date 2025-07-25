# Technical Analysis Library

## Introduction

This lib is refactored from [finta](https://github.com/peerchemist/finta/tree/master) by [peerchemist](https://github.com/peerchemist)

## Usage Examples

### Simple Usage

```python
from talib import TA

# Load OHLCV data
df = pd.read_csv('ohlcv_data.csv')


# With OHLC data
ta = TA(ohlc=df)
print(ta.available_indicators)  # Shows all indicators


# Calculate indicators
sma = ta.SMA(period=20)  
rsi_14 = ta.RSI(14)
macd = ta.MACD()
heikin_ashi = ta.HEIKIN_ASHI()
```


## Kaggle

- Kaggle package: [talib2025](https://www.kaggle.com/datasets/xxxxyyyy80008/talib2025)
- Kaggle examples: [2025 talib examples](https://www.kaggle.com/code/xxxxyyyy80008/2025-talib-examples/)