# Placeholder for loading clinical time-series data
import pandas as pd

def load_dummy_data():
    # This function should be replaced with actual ICU data loader
    return pd.DataFrame({
        'time': [0, 1, 2, 3],
        'heart_rate': [80, 85, 90, 88],
        'bp': [120, 118, 115, 117]
    })
