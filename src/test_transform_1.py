import pandas as pd
import pytest
from transform_1 import transform_data_1

def test_transform_data_1():
    # Create a sample DataFrame
    data = {'A': [1, 2, None], 'B': [4, None, 6]}
    df = pd.DataFrame(data)
    print(df)
    # Apply the transformation
    transformed_df = transform_data_1(df)
    
    # Assert there are no NaN values
    assert transformed_df.isna().sum().sum() == 0
    # Assert all columns are lowercase
    assert all(col.islower() for col in transformed_df.columns)
