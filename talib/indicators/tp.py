import pandas as pd
from talib.base import OHLCIndicator, register_indicator

@register_indicator
class TP(OHLCIndicator):
    """Typical Price"""
    def __init__(self, source, **kwargs):
        super().__init__(source, **kwargs)
        
    def compute(self) -> pd.Series:
        high, low, close = self.data['high'], self.data['low'], self.data['close']   
        return ((high + low +  close) / 3).rename("TP")
