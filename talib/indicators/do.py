import pandas as pd
from talib.base import OHLCIndicator, register_indicator

@register_indicator
class DO(OHLCIndicator):
    """Donchian Channel"""
    def __init__(self, source, upper_period: int = 20, lower_period: int = 5, **kwargs):
        super().__init__(source, **kwargs)
        self.upper_period = upper_period
        self.lower_period = lower_period
        
    def compute(self) -> pd.DataFrame:
        high, low = self.data['high'], self.data['low']
        upper = high.rolling(center=False, window=self.upper_period).max()
        lower = low.rolling(center=False, window=self.lower_period).min()
        middle = (upper + lower) / 2
    
        return pd.DataFrame({
            'UPPER': upper,
            'LOWER': lower,
            'MIDDLE': middle
        })
