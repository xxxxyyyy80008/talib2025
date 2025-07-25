import pandas as pd
from talib.base import OHLCVIndicator, register_indicator


@register_indicator
class VWAP(OHLCVIndicator):
    """
    Volume Weighted Average Price
    
    A trading benchmark calculated by adding up the dollars traded for every 
    transaction (price × volume) and dividing by the total volume traded.
    """
    
    def __init__(self, 
                 source: pd.DataFrame,
                 **kwargs):
        """
        Initialize VWAP indicator
        
        :param source: OHLCV DataFrame
        :param kwargs: Additional parameters passed to parent class
        """
        super().__init__(source, **kwargs)
        
    def compute(self) -> pd.Series:
        """
        Compute the volume weighted average price
        
        :return: Series containing the VWAP values
        """
        # Calculate typical price if not using close price
        tp = (self.data['high'] + self.data['low'] + self.data['close']) / 3
        
        # Calculate cumulative dollar volume and cumulative volume
        cum_dollar_volume = (tp * self.data['volume']).cumsum()
        cum_volume = self.data['volume'].cumsum()
        
        return pd.Series(
            cum_dollar_volume / cum_volume,
            name="VWAP"
        )