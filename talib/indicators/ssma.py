import pandas as pd
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class SSMA(SeriesIndicator):
    """Smoothed simple moving average"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        return self.series.ewm(ignore_na=False, alpha=1.0 / self.period, min_periods=0).mean().rename(f"SSMA{self.period}")
