# -*- coding: utf-8 -*-
"""data_convert.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SZcPxQ6JLzrba4kg5SEnpUao0p_Lh7SU
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define constants for special tokens
SOS_token = 0
EOS_token = 1

# Function to convert word to tensor of indices
def tensorFromWord(lang, word):
    indexes = [lang.word2index[char] for char in word]
    indexes.append(EOS_token)
    return torch.tensor(indexes, dtype=torch.long, device=device).view(-1, 1)

# Function to prepare tensors from pairs
def tensorsFromPair(input_lang, output_lang, pair):
    input_tensor = tensorFromWord(input_lang, pair[0])
    target_tensor = tensorFromWord(output_lang, pair[1])
    return input_tensor, target_tensor