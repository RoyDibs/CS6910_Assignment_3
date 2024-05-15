# -*- coding: utf-8 -*-
"""train_model.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1-cvGboqBsAiNaHw2508O4hd2DDnO159K
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import argparse

from data_loader_functions import  load_data, prepare_data, get_cell, get_optimizer
from model import Encoder, Decoder
from data_convert import tensorFromWord, tensorsFromPair
from train import train
from test import test


parser = argparse.ArgumentParser(description="Train neural network with specified hyperparameters.")


parser.add_argument("-em_z", "--embed_size", type=int, default=32, help="Embedding size for word vectors")
parser.add_argument("-hd_z", "--hidden_size", type=int, default=512, help="Hidden size for LSTM/GRU cells")
parser.add_argument("-cell", "--cell_type", default="RNN", choices=["LSTM", "GRU", "RNN"], help="Type of recurrent cell (LSTM or GRU)")
parser.add_argument("-n_l","--num_layers", type=int, default=1, help="Number of stacked LSTM/GRU layers")
parser.add_argument("-dp", "--dropout", type=float, default=0, help="Dropout rate for regularization")
parser.add_argument("-lr", "--learning_rate", type=float, default=0.001, help="Learning rate for the optimizer")
parser.add_argument("-o", "--optimizer", default="Adam", choices=["Adam"], help="Optimizer used for training (currently only Adam supported)")
parser.add_argument("-e","--epochs", type=int, default=5, help="Number of epochs to train the network")
parser.add_argument("-dir","--data_dir", type=str, required=True, help="Directory path containing the training dataset")

args = parser.parse_args()

# Set device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def train_model(input_lang, output_lang, pairs, config):
    # Initialize encoder and decoder
    encoder = Encoder(input_lang.n_words, config['embed_size'], config['hidden_size'], config['cell_type'], config['num_layers'], config['dropout']).to(device)
    decoder = Decoder(output_lang.n_words, config['embed_size'], config['hidden_size'], config['cell_type'], config['num_layers'], config['dropout']).to(device)

    # Define optimizer and criterion
    encoder_optimizer = get_optimizer(config['optimizer'])(encoder.parameters(), lr=config['learning_rate'])
    decoder_optimizer = get_optimizer(config['optimizer'])(decoder.parameters(), lr=config['learning_rate'])
    criterion = nn.NLLLoss()

    # Training loop
    for epoch in range(config['epochs']):
        total_loss = 0
        for pair in pairs:
            input_tensor, target_tensor = tensorsFromPair(input_lang, output_lang, pair)
            loss = train(input_tensor, target_tensor, encoder, decoder, encoder_optimizer, decoder_optimizer, criterion)
            total_loss += loss

        #training loss
        print(f"Epoch: {epoch + 1}")
        print(f"Training Loss: {total_loss / len(pairs)}")

    # Test the model
    validation_accuracy = test(encoder, decoder, input_lang, output_lang, output_lang.name, "valid", path)
    print(f"validation_accuracy: {validation_accuracy}")



config = {

    'embed_size': args.embed_size,
    'hidden_size': args.hidden_size,
    'cell_type': args.cell_type,
    'num_layers': args.num_layers,
    'dropout': args.dropout,
    'learning_rate': args.learning_rate,
    'optimizer': args.optimizer,
    'epochs': args.epochs
}

path = args.data_dir
# Load data and prepare languages
input_lang, output_lang, pairs = prepare_data('hin', path)
train_model(input_lang, output_lang, pairs, config)

