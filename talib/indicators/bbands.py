import pandas as pd
from typing import Optional
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class BBANDS(SeriesIndicator):
    """
    Bollinger Bands® - volatility bands placed above and below a moving average.
    Developed by John Bollinger.
    
    Allows input of any moving average series (SMA, EMA, KAMA, etc) around which
    bands will be formed.
    """
    def __init__(self, source, 
                period: int = 20, 
                ma: Optional[pd.Series] = None,
                std_multiplier: float = 2, **kwargs):
        """
        :param period: Period for standard deviation calculation
        :param ma: Optional moving average series to use as middle band
        :param std_multiplier: Multiplier for standard deviation bands
        :return: DataFrame with BB_UPPER, BB_MIDDLE, BB_LOWER columns
        """
        super().__init__(source, **kwargs)
        self.period = period
        self.ma = ma
        self.std_multiplier = std_multiplier

    def compute(self) -> pd.DataFrame:
        # Calculate standard deviation
        std = self.series.rolling(window=self.period).std()
        
        # Determine middle band
        if self.ma is not None:
            middle_band = pd.Series(self.ma, name="BB_MIDDLE")
        else:
            middle_band = pd.Series(
                self.series.rolling(window=self.period).mean(), 
                name="BB_MIDDLE"
            )
        
        # Calculate bands
        upper_bb = pd.Series(
            middle_band + (self.std_multiplier * std), 
            name="BB_UPPER"
        )
        lower_bb = pd.Series(
            middle_band - (self.std_multiplier * std), 
            name="BB_LOWER"
        )
        
        return pd.concat([upper_bb, middle_band, lower_bb], axis=1)
