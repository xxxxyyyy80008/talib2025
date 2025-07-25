import pandas as pd
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class TRIX(SeriesIndicator):
    """TRIX indicator: the rate of change of a triple exponential moving average"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        m = self.series.ewm(span=self.period).mean().ewm(span=self.period).mean().ewm(span=self.period).mean()
        return (100 * (m.diff() / m)).rename(f"TRIX{self.period}")
