# indicators/__init__.py
import os
import importlib
import inspect
import sys
from pathlib import Path
from typing import Dict, Type
import pandas as pd
from ..core import TA, Indicator, SeriesIndicator, OHLCIndicator, OHLCVIndicator


# Dictionary to hold all available indicator classes
INDICATORS = {}

# Auto-discover and register all indicator classes in this package
package_dir = Path(__file__).parent

for module_file in package_dir.glob("*.py"):
    if module_file.name == "__init__.py":
        continue
    
    module_name = module_file.stem
    try:
        module = importlib.import_module(f".{module_name}", package=__name__)
        
        for name, obj in module.__dict__.items():
            INDICATORS[name] = obj
    except ImportError as e:
        print(f"Warning: Could not import module {module_name}: {e}")

# Make all indicators directly available when importing the package
__all__ = list(INDICATORS.keys()) + ["INDICATORS"]
globals().update(INDICATORS)
