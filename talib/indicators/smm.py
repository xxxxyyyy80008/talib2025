import pandas as pd
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class SMM(SeriesIndicator):
    """Simple moving median"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        return self.series.rolling(window=self.period).median().rename(f"SMM{self.period}")
        