# -*- coding: utf-8 -*-
"""evaluate.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1o2y7MkPUVjaySLP0Cyp5j-m0SiOKQN5H
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np

from data_convert import tensorFromWord, tensorsFromPair

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define constants for special tokens
SOS_token = 0
EOS_token = 1

# Function to evaluate the model
def evaluate(encoder, decoder, word, input_lang, output_lang, max_length=50):
    with torch.no_grad():
        input_tensor = tensorFromWord(input_lang, word)
        input_length = input_tensor.size()[0]
        encoder_hidden = encoder.initHidden()

        for ei in range(input_length):
            encoder_output, encoder_hidden = encoder(input_tensor[ei], encoder_hidden)

        decoder_input = torch.tensor([[SOS_token]], device=device)
        decoder_hidden = encoder_hidden

        decoded_chars = ""

        for di in range(max_length):
            decoder_output, decoder_hidden = decoder(decoder_input, decoder_hidden)
            topv, topi = decoder_output.topk(1)

            if topi.item() == EOS_token:
                break
            else:
                decoded_chars += output_lang.index2word[topi.item()]

            decoder_input = topi.squeeze().detach()

        return decoded_chars