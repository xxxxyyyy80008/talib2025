import pandas as pd
import numpy as np
from talib.base import OHLCIndicator, register_indicator

@register_indicator
class ATR(OHLCIndicator):
    """Average True Range"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period

    def compute(self) -> pd.Series:
        high, low, close = self.data['high'], self.data['low'], self.data['close']
        tr1 = high - low
        tr2 = (high - close.shift()).abs()
        tr3 = (low - close.shift()).abs()
        tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)
        return tr.rolling(self.period).mean().rename(f"ATR{self.period}")
