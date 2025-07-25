import pandas as pd
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class TRIMA(SeriesIndicator):
    """Triangular Moving Average (TRIMA) [also known as TMA]"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        return (self.series.rolling(window=self.period).mean()\
                    .rolling(window=self.period).sum()/self.period).rename(f"TRIMA{self.period}")
