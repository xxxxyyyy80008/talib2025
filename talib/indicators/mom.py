import pandas as pd
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class MOM(SeriesIndicator):
    """momentum"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        return self.series.diff(self.period).rename(f"MOM{self.period}")