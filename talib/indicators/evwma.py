import pandas as pd
from talib.base import OHLCVIndicator, register_indicator

@register_indicator
class EVWMA(OHLCVIndicator):
    """
    Elastic Volume Weighted Moving Average
    
    An approximation of the average price paid per share in the last n periods,
    with weights that adjust based on volume changes.
    
    Parameters:
    -----------
    period : int
        The number of periods to average over (default 20)
    """
    
    def __init__(self, 
                 source: pd.DataFrame,
                 period: int = 20,
                 **kwargs):
        """
        Initialize EVWMA indicator
        
        :param source: OHLCV DataFrame
        :param period: Moving average window size (default 20)
        :param kwargs: Additional parameters passed to parent class
        """
        super().__init__(source,  **kwargs)
        self.period = period
        
    def compute(self) -> pd.Series:
        """
        Compute the elastic volume weighted moving average
        
        :return: Series containing the EVWMA values
        """
        vol_sum = self.data['volume'].rolling(window=self.period).sum()
        x = (vol_sum - self.data['volume']) / vol_sum
        y = (self.data['volume'] * self.data['close']) / vol_sum
        
        evwma = [0.0]
        
        for xi, yi in zip(x.fillna(0).values, y.fillna(0).values):
            if xi == 0 or yi == 0:
                evwma.append(0.0)
            else:
                evwma.append(evwma[-1] * xi + yi)
        
        return pd.Series(
            evwma[1:], 
            index=self.data.index, 
            name=f"EVWMA{self.period} "
        )