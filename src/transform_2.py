import pandas as pd

def transform_data_2(df):
    # Replace NaN values with the mean
    df = df.fillna(df.mean())

    # Add a new column that is the sum of all numerical columns
    df['sum'] = df.select_dtypes(include='number').sum(axis=1)
    return df
