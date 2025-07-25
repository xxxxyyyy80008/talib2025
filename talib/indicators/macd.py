import pandas as pd
from talib.base import SeriesIndicator, register_indicator

@register_indicator
class MACD(SeriesIndicator):
    """Moving Average Convergence Divergence"""
    def __init__(self, source, fast: int = 12, slow: int = 26, signal: int = 9, **kwargs):
        super().__init__(source, **kwargs)
        self.fast = fast
        self.slow = slow
        self.signal = signal
        
    def compute(self) -> pd.DataFrame:
        fast_ema = self.series.ewm(span=self.fast, min_periods=self.fast).mean()
        slow_ema = self.series.ewm(span=self.slow, min_periods=self.slow).mean()
        macd_line = fast_ema - slow_ema
        signal_line = macd_line.ewm(span=self.signal, min_periods=self.signal).mean()
        histogram = macd_line - signal_line
        return pd.DataFrame({
            'MACD': macd_line,
            'SIGNAL': signal_line,
            'HISTOGRAM': histogram
        })
