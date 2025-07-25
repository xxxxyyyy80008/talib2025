import pandas as pd
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class ZLEMA(SeriesIndicator):
    """Zero Lag Exponential Moving Average"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        lag = int((self.period - 1) / 2)
        return ((self.series + self.series.diff(lag)).ewm(span=self.period).mean()).rename(f"ZLEMA{self.period}")
