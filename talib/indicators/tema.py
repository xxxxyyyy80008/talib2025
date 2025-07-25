import pandas as pd
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class TEMA(SeriesIndicator):
    """ Triple exponential moving average"""
    def __init__(self, source, period=14, **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        ema = self.series.ewm(span=self.period, min_periods=self.period).mean()
        ema_2t = ema.ewm(ignore_na=False, span=self.period).mean()
        ema_3t = ema_2t.ewm(ignore_na=False, span=self.period).mean()
        return (3*ema - 3*ema_2t + ema_3t).rename(f"TEMA{self.period}")
