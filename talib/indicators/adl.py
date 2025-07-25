import pandas as pd
from talib.base import OHLCIndicator, register_indicator

@register_indicator
class ADL(OHLCIndicator):
    """accumulation/distribution line"""
    def __init__(self, source, **kwargs):
        super().__init__(source, **kwargs)
        
    def compute(self) -> pd.Series:
        mfm = ((self.data["close"] - self.data["low"])
            - (self.data["high"] - self.data["close"])) / (self.data["high"] - self.data["low"])
        return (mfm*self.data["volume"]).rename("MFV")
