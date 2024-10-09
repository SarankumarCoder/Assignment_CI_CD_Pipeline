import pandas as pd
import pytest
from transform_2 import transform_data_2

def test_transform_data_2():
    # Create a sample DataFrame
    data = {'A': [1, 2, None], 'B': [4, None, 6]}
    df = pd.DataFrame(data)
    
    # Apply the transformation
    transformed_df = transform_data_2(df)
    
    # Assert NaN values are replaced with the mean
    assert transformed_df.isna().sum().sum() == 0
    assert transformed_df['A'][2] == 1.5
    # assert transformed_df['B'][1] == 5.0

    # Assert 'sum' column exists
    assert 'sum' in transformed_df.columns
