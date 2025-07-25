import pandas as pd
from talib.base import OHLCIndicator, register_indicator

@register_indicator
class VW_MACD(OHLCIndicator):
    """Moving Average Convergence Divergence"""
    def __init__(self, source, fast: int = 12, slow: int = 26, signal: int = 9, column: str = "close", **kwargs):
        super().__init__(source, **kwargs)
        self.fast = fast
        self.slow = slow
        self.signal = signal
        self.column = column
        
    def compute(self) -> pd.DataFrame:
        vp = self.data['volume'] * self.data[self.column]
        fast_ema = (vp.ewm(span=self.fast, min_periods=self.fast).mean())/(self.data['volume'].ewm(span=self.fast, min_periods=self.fast).mean())
        slow_ema = (vp.ewm(span=self.slow, min_periods=self.slow).mean())/(self.data['volume'].ewm(span=self.slow, min_periods=self.slow).mean())
        
        macd_line = fast_ema - slow_ema
        signal_line = macd_line.ewm(span=self.signal, min_periods=self.signal).mean()
        histogram = macd_line - signal_line
        return pd.DataFrame({
            'VW_MACD': macd_line,
            'VW_SIGNAL': signal_line,
            'VW_HISTOGRAM': histogram
        })
