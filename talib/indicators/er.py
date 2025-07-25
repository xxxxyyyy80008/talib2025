import pandas as pd
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class ER(SeriesIndicator):
    """Kaufman Efficiency indicator"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        chg = self.series.diff(self.period).abs()
        vol = self.series.diff().abs().rolling(window=self.period).sum()
        return (chg/vol).rename(f"ER{self.period}")