from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")
RAW = DATA_DIR / "raw"
PROCESSED = DATA_DIR / "processed"

def read_csv(name: str, **kwargs) -> pd.DataFrame:
    """Read a CSV from data/raw by file name."""
    return pd.read_csv(RAW / name, **kwargs)

def save_processed(df: pd.DataFrame, name: str, index=False):
    """Save a DataFrame into data/processed by file name."""
    PROCESSED.mkdir(parents=True, exist_ok=True)
    df.to_csv(PROCESSED / name, index=index)
