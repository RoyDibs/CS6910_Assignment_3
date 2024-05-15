# -*- coding: utf-8 -*-
"""train_single.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18k9TMMu9Ju9Fjo6PdaUcwX2c5_aHacPQ
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import random

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Define constants for special tokens
SOS_token = 0
EOS_token = 1

def train_single(model, input_tensor, target_tensor):
    encoder_hidden = model.encoder.init_hidden()
    encoder_cell = model.encoder.init_hidden()
    model.encoder_optimizer.zero_grad()
    model.decoder_optimizer.zero_grad()
    input_length = input_tensor.size(0)
    target_length = target_tensor.size(0)
    encoder_outputs = torch.zeros(model.max_length, model.encoder.hidden_size, device=device)
    loss = 0
    for ei in range(input_length):
        encoder_output, encoder_hidden, encoder_cell = model.encoder(input_tensor[ei], encoder_hidden, encoder_cell)
        encoder_outputs[ei] = encoder_output[0, 0]
    decoder_input = torch.tensor([[SOS_token]], device=device)
    decoder_hidden, decoder_cell = encoder_hidden, encoder_cell
    use_teacher_forcing = True if random.random() < model.teacher_forcing_ratio else False
    if use_teacher_forcing:
        for di in range(target_length):
            decoder_output, decoder_hidden, decoder_cell, _ = model.decoder(decoder_input, decoder_hidden, decoder_cell, encoder_outputs)
            loss += model.criterion(decoder_output, target_tensor[di])
            decoder_input = target_tensor[di]
    else:
        for di in range(target_length):
            decoder_output, decoder_hidden, decoder_cell, _ = model.decoder(decoder_input, decoder_hidden, decoder_cell, encoder_outputs)
            loss += model.criterion(decoder_output, target_tensor[di])
            topv, topi = decoder_output.topk(1)
            decoder_input = topi.squeeze().detach()
            if decoder_input.item() == EOS_token:
                break
    loss.backward()
    model.encoder_optimizer.step()
    model.decoder_optimizer.step()
    return loss.item() / target_length