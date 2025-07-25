import pandas as pd
import numpy as np
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class CMO(SeriesIndicator):
    """Chande Momentum Oscillator (CMO)"""
    def __init__(self, source, period: int = 9, factor: int = 100, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        self.factor = factor

    def compute(self) -> pd.Series:
        delta = self.series.diff()
        gains = delta.clip(lower=0)
        losses = -delta.clip(upper=0)
       
        # EMAs of gains and losses
        avg_gain = gains.ewm(com=self.period, min_periods=self.period).mean()
        avg_loss = losses.ewm(com=self.period, min_periods=self.period).mean()
              
        return (self.factor * ((avg_gain - avg_loss) / (avg_gain + avg_loss))).rename(f"CMO{self.period}")
