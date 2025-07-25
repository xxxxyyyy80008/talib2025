# indicators/kc.py
import pandas as pd
from typing import Optional
from talib.base import OHLCIndicator, register_indicator
from .ema import EMA
from .atr import ATR

@register_indicator
class KC(OHLCIndicator):
    """Keltner Channels"""
    def __init__(self, source, 
                period: int = 20, 
                atr_period: int = 10, 
                ma: Optional[pd.Series] = None, 
                kc_mult: float = 2, **kwargs):
        """
        Calculate Keltner Channels
        :param period: Period for middle line EMA
        :param atr_period: Period for ATR calculation
        :param ma: Optional moving average series to use instead of EMA
        :param kc_mult: Multiplier for ATR bands
        :return: DataFrame with KC_UPPER and KC_LOWER columns
        """
        super().__init__(source, **kwargs)
        self.period = period
        self.atr_period = atr_period
        self.ma = ma
        self.kc_mult = kc_mult
        
    def compute(self) -> pd.DataFrame:
        # Calculate or use provided moving average
        if self.ma is not None:
            middle = pd.Series(self.ma, name="KC_MIDDLE")
        else:
            ema = EMA(self.data, column=self.column)
            middle = pd.Series(ema.compute(self.period), name="KC_MIDDLE")
        
        # Calculate ATR
        atr_ind = ATR(self.data)
        atr_series = atr_ind.compute(self.atr_period)
        
        # Calculate bands
        up = pd.Series(middle + (self.kc_mult * atr_series), name="KC_UPPER")
        down = pd.Series(middle - (self.kc_mult * atr_series), name="KC_LOWER")
        
        return pd.concat([up, down], axis=1)

