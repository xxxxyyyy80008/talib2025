import pandas as pd
import numpy as np
from talib.base import OHLCIndicator, register_indicator

@register_indicator
class OBV(OHLCIndicator):
    """On-Balance Volume"""
    def __init__(self, source, **kwargs):
        super().__init__(source, **kwargs)
        
    def compute(self) -> pd.Series:
        return (np.sign(self.data['close'].diff()) * self.data['volume']).cumsum()
