import pandas as pd
from talib.base import OHLCIndicator, register_indicator
from .adl import ADL

@register_indicator
class CHAIKIN(OHLCIndicator):
    """Chaikin Oscillator"""
    def __init__(self, source,  **kwargs):
        super().__init__(source, **kwargs)
        
    def compute(self) -> pd.Series:
        adl_series = ADL(self.data).compute()
        return (adl_series.ewm(span=3, min_periods=2).mean()
                    - adl_series.ewm(span=10, min_periods=9).mean()).rename("CHAIKIN")


