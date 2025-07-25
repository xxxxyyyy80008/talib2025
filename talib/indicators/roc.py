import pandas as pd
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class ROC(SeriesIndicator):
    """Rate-of-Change (ROC)"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        return (self.series.pct_change(self.period)).rename(f"ROC{self.period}")

##(self.series.diff(period)/self.series.shift(period)).rename(f"ROC{period}")