import pandas as pd
import numpy as np
from talib.base import OHLCIndicator, register_indicator

@register_indicator
class VZO(OHLCIndicator):
    """VZO"""
    def __init__(self, source, period=14, column: str = "close", **kwargs):
        super().__init__(source, **kwargs)
        self.period = period
        self.column = column
        
    def compute(self) -> pd.Series:
        dvma = (np.sign(self.data[self.column].diff()) * self.data["volume"]).ewm(span=self.period).mean()
        vma = self.data["volume"].ewm(span=self.period).mean()

        return (100 * (dvma / vma)).rename(f"VZO{self.period}")