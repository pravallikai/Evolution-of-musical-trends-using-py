import pandas as pd

def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Make column names simple and consistent:
    - trim spaces
    - lowercase
    - replace spaces with underscores
    - remove symbols
    """
    df = df.copy()
    df.columns = (
        df.columns
          .str.strip()
          .str.lower()
          .str.replace(" ", "_")
          .str.replace("[^a-z0-9_]", "", regex=True)
    )
    return df
