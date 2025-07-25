import pandas as pd
from talib.base import OHLCIndicator, register_indicator

@register_indicator
class HEIKIN_ASHI(OHLCIndicator):
    """Heikin-Ashi Candlestick"""
    def __init__(self, source, **kwargs):
        super().__init__(source, **kwargs)
        
    def compute(self) -> pd.DataFrame:
        ha_df = pd.DataFrame(index=self.data.index)
        
        # Close = (open + high + low + close)/4
        ha_df['close'] = (self.data['open'] + self.data['high'] + 
                          self.data['low'] + self.data['close']) / 4
        
        # Open = (previous open + previous close)/2
        ha_df['open'] = (self.data['open'].shift(1) + self.data['close'].shift(1)) / 2
        ha_df.loc[ha_df.index[0], 'open'] = (self.data['open'].iloc[0] + self.data['close'].iloc[0]) / 2
        
        # High = max(high, open, close)
        ha_df['high'] = self.data[['high', 'open', 'close']].max(axis=1)
        
        # Low = min(low, open, close)
        ha_df['low'] = self.data[['low', 'open', 'close']].min(axis=1)
        
        return ha_df[['open', 'high', 'low', 'close']]
