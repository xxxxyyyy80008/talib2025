import pandas as pd
from talib.base import OHLCIndicator, register_indicator

@register_indicator
class ICHIMOKU(OHLCIndicator):
    """Ichimoku Cloud"""
    def __init__(self, source, tenkan_period: int = 9, kijun_period: int = 26,
        senkou_period: int = 52, chikou_period: int = 26, **kwargs):
        super().__init__(source, **kwargs)
        self.tenkan_period = tenkan_period
        self.kijun_period = kijun_period
        self.senkou_period = senkou_period
        self.chikou_period = chikou_period
        
    def compute(self) -> pd.DataFrame:
        high, low = self.data['high'], self.data['low']
        
        # Conversion Line (Tenkan-sen) "TENKAN"
        tenkan_sen =  (high.rolling(window=self.tenkan_period).max() + low.rolling(window=self.tenkan_period).min())/ 2
            
        # Base Line (Kijun-sen) #"KIJUN"
        kijun_sen = ( high.rolling(window=self.kijun_period).max() + low.rolling(window=self.kijun_period).min()) / 2 ## base line
        
        # Leading Span A (Senkou Span A) ## Leading span "senkou_span_a"
        senkou_span_a = ((tenkan_sen + kijun_sen) / 2).shift(self.kijun_period) 
      
        # Leading Span B (Senkou Span B) #"SENKOU"
        senkou_span_b = ((high.rolling(window= self.senkou_period).max() + low.rolling(window= self.senkou_period).min()) / 2).shift(self.kijun_period) 
                   
        # Lagging Span (Chikou Span) # "CHIKOU"
        chikou_span =  self.data['close'].shift(- self.chikou_period) 

        return pd.DataFrame({
            'TENKAN': tenkan_sen, #conversion
            'KIJUN': kijun_sen, #base
            'senkou_span_a': senkou_span_a, #leading_span_a
            'SENKOU': senkou_span_b, #leading_span_b
            'CHIKOU': chikou_span #lagging_span
        })
                   
'''
class ICHIMOKU(OHLCIndicator):
    """Ichimoku Cloud"""
    def compute(self, conversion_period: int = 9, base_period: int = 26, 
               leading_span_period: int = 52, displacement: int = 26) -> pd.DataFrame:
        high, low = self.data['high'], self.data['low']
        
        # Conversion Line (Tenkan-sen)
        conversion = (high.rolling(conversion_period).max() + 
                     low.rolling(conversion_period).min()) / 2
        
        # Base Line (Kijun-sen)
        base = (high.rolling(base_period).max() + 
               low.rolling(base_period).min()) / 2
        
        # Leading Span A (Senkou Span A)
        leading_span_a = ((conversion + base) / 2).shift(displacement)
        
        # Leading Span B (Senkou Span B)
        leading_span_b = ((high.rolling(leading_span_period).max() + 
                          low.rolling(leading_span_period).min()) / 2).shift(displacement)
        
        # Lagging Span (Chikou Span)
        lagging_span = self.data['close'].shift(-displacement)
        
        return pd.DataFrame({
            'conversion': conversion,
            'base': base,
            'leading_span_a': leading_span_a,
            'leading_span_b': leading_span_b,
            'lagging_span': lagging_span
        })
'''
