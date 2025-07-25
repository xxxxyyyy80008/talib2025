import pandas as pd
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class DEMA(SeriesIndicator):
    """Double Exponential Moving Average"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        ema = self.series.ewm(span=self.period, min_periods=self.period).mean()
        dema = 2*ema - ema.ewm(span=self.period, min_periods=self.period).mean()
        return dema.rename(f"DEMA{self.period}")
