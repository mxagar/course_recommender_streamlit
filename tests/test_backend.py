'''This module tests the functions in the module backend.py.

Note that the testing configuration fixtures
are located in `conftest.py`.

To install pytest:
>> pip install -U pytest

The script expects the proper datasets to be located in `./data`.

Author: Mikel Sagardia
Date: 2023-02-15
'''

#import os
#from os import listdir
#import numpy as np
import pytest

# IMPORTANT: the file conftest.py defines the fixtures used in here
# and it contains the necessary imports!

### -- Tests -- ###

def test_load_ratings(load_ratings):
    """Test load_ratings() function."""
    ratings_df = load_ratings()
    
    # Data frames
    try:
        assert ratings_df.shape[0] > 0
        assert ratings_df.shape[1] > 0
    except AssertionError as err:
        print("TESTING load_ratings(): ERROR - Data frame has no rows / columns.")
        raise err
