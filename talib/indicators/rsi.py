import pandas as pd
import numpy as np
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class RSI(SeriesIndicator):
    """Relative Strength Index"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        delta = self.series.diff()
        gains = delta.clip(lower=0)
        losses = -delta.clip(upper=0)
        # avg_gain = gains.rolling(period).mean()
        # avg_loss = losses.rolling(period).mean()
        # EMAs of gains and losses
        avg_gain = gains.ewm(alpha=1.0 / self.period).mean()
        avg_loss = losses.ewm(alpha=1.0 / self.period).mean()
        # EMAs - alternative
        # avg_gain = gains.ewm(com=period-1, min_periods=period).mean()
        # avg_loss = losses.ewm(com=period-1, min_periods=period).mean()
        rs = avg_gain / avg_loss 
      
        return (100 - (100 / (1 + rs))).rename(f"RSI{self.period}")
