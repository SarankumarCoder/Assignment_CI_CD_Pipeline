import pandas as pd

def transform_data_1(df):
    # Drop any rows with NaN values
    df = df.dropna()
    
    # Convert all column names to lowercase
    df.columns = [col.lower() for col in df.columns]
    return df
