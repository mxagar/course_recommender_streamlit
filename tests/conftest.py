'''Testing configuration module for Pytest.
This file is read by pytest and the fixtures
defined in it are used in all the tested files.

Author: Mikel Sagardia
Date: 2023-02-15
'''

import pytest

#import logging
import backend as bck

## -- Parameters

@pytest.fixture
def model_names():
    '''Model names'''
    return bck.MODELS

## -- Functions

@pytest.fixture
def load_ratings():
    '''load_ratings() function from backend.'''
    return bck.load_ratings
