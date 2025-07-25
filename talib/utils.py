import pandas as pd
from typing import Dict, Union

# Common column name variants
COLUMN_VARIANTS = {
    'open': ['open', 'opening_price', 'o', 'open_price'],
    'high': ['high', 'highest', 'h', 'high_price', 'max_price'],
    'low': ['low', 'lowest', 'l', 'low_price', 'min_price'],
    'close': ['close', 'closing_price', 'c', 'last_price', 'price', 'last'],
    'volume': ['volume', 'vol', 'v', 'trading_volume', 'turnover']
}

def standardize_ohlcv_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Rename variant column names to standard OHLCV names
    :param df: Input DataFrame with financial data
    :return: DataFrame with standardized column names
    """
    # Create reverse mapping from variant to standard name
    rename_map = {}
    for standard, variants in COLUMN_VARIANTS.items():
        for variant in variants:
            rename_map[variant] = standard
    
    # Create case-insensitive mapping
    rename_map = {col.lower(): standard for col, standard in rename_map.items()}
    
    # Generate actual rename dictionary for columns that exist
    actual_rename = {}
    for col in df.columns:
        col_lower = col.lower()
        if col_lower in rename_map:
            actual_rename[col] = rename_map[col_lower]
    
    # Apply renaming
    df = df.rename(columns=actual_rename)
    
    return df

def validate_ohlcv(df: pd.DataFrame, require_volume: bool = False):
    """
    Validate OHLCV DataFrame structure
    :param df: DataFrame to validate
    :param require_volume: Whether volume column is required
    """
    required = ['open', 'high', 'low', 'close']
    if require_volume:
        required.append('volume')
    
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
