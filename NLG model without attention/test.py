# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nzSLjt4osNBqh5_nTSq_l_OUDmh48u2x
"""

import torch
import torch.nn as nn
import numpy as np

from data_loader_functions import  load_data
from evaluate import evaluate

# Function to test the model
def test(encoder, decoder, input_lang, output_lang, language, data_type, path):
    pairs = load_data(language, data_type, path)
    accuracy = np.sum([evaluate(encoder, decoder, pair[0], input_lang, output_lang) == pair[1] for pair in pairs])
    return accuracy / len(pairs)