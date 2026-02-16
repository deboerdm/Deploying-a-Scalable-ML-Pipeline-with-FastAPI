import pytest

# TODO: add necessary import

import numpy as np
import pandas as pd
import os
from ml.model import inference, train_model
from sklearn.model_selection import train_test_split

# TODO: implement the first test. Change the function name and input as needed
def test_inference_function():
    """
    # Testing the inference function
    """
    X = np.random.rand(20, 5)
    y = np.random.randint(5, size=20)
    model = train_model(X, y)
    y_preds = inference(model, X)
    assert y.shape == y_preds.shape


# TODO: implement the second test. Change the function name and input as needed
def test_model_encoder_saved():
    """
    # Testing if model and encoder were saved to correct location
    """
    model_path = os.path.join('model','model.pkl')
    encoder_path = os.path.join('model','encoder.pkl')
    assert os.path.isfile(model_path)
    assert os.path.isfile(encoder_path)



# TODO: implement the third test. Change the function name and input as needed
def test_train_test_split_sizes():
    """
    # testing datasets for expected size
    """
    data_path = os.path.join('data','census.csv')
    data = pd.read_csv(data_path)
    train, test = train_test_split(data, test_size=0.2)
    assert train.shape[0] <= np.ceil(data.shape[0] * 0.8)
    assert test.shape[0] <= np.ceil(data.shape[0] * 0.2)

