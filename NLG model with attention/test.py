# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LPKKc4fw0-BuS0bjeaGZDh41hxaqiVHE
"""

import torch
import torch.nn as nn
import numpy as np

from data_loader_functions import  load_data
from evaluate import evaluate

def test_validate(model, type:str, path):
    pairs = load_data(model.lang, type, path)
    accuracy = 0
    for pair in pairs:
        output = evaluate(model, pair[0])
        if output == pair[1]:
            accuracy += 1
    return accuracy / len(pairs)