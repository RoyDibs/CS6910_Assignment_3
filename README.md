# CS6910_Assignment_-3

This repository contains the Python files used to generate the results presented in the accompanying report. For detailed insights, please refer to the report available [here](https://api.wandb.ai/links/dibakar/y23lbm87).

## Instruction to run the py file:

### Usage

#### NLG model without attention

``` NLG model without attention ``` is the folder that contains the functions to run a seq2seq model with no attention mechanism.
The train_model.py file is the main function that can be called to run the code. To run the train_model.py file, you can use the following command-line arguments:

```bash
python train_model.py -em_z <embed_size> -hd_z <hidden_size> -cell <cell_type> -n_l <activation> -nf <num_layers> -dp <dropout> -lr <learning_rate> -o <optimizer> -e <epochs> -tfr <teacher_forcing_ratio> -m_l <max_length> -dir <data_dir>
```

##### Command-line Arguments

- `-em_z`, `--embed_size`: Embedding size for word vectors (default: 32).
- `-hd_z`, `--hidden_size`: Hidden size for LSTM/GRU/RNN cells (default: 512).
- `-lr`, `--learning_rate`: Learning rate (default: 0.001).
- `-cell`, `--cell_type`: Type of recurrent cell (default: 'RNN'). Choices: "LSTM", "GRU", "RNN".
- `-n_l`, `--num_layers`: Number of stacked LSTM/GRU/RNN layers (default: 1).
- `-dp`, `--dropout`: Dropout rate for regularization (default: 0).
- `-0`, `--optimizer`: Optimizer used for training (default: 'ADAM').
- `-e`, `--epochs`: Number of epochs to train the network (default: 5).
- `-tfr`, `--teacher_forcing_ratio`: teacher_forcing_ratio (default: 0.5). 
- `-m_l`, `--max_length`: Maximum length (default: 50).
- `-dir`, `--data_dir`: Directory path containing the training dataset **required**

**Note**: Replace `<embed_size>`, `<hidden_size>`, `<learning_rate>`, and other placeholders with appropriate values.

#### NLG model with attention

``` NLG model without attention ``` is the folder that contains the functions to run a seq2seq model with an attention mechanism.
The train_model.py file is the main function that can be called to run the code. To run the train_model.py file, you can use the following command-line arguments:

```bash
python train_model.py -em_z <embed_size> -hd_z <hidden_size> -cell <cell_type> -n_l <activation> -nf <num_layers> -dp <dropout> -lr <learning_rate> -o <optimizer> -e <epochs> -tfr <teacher_forcing_ratio> -m_l <max_length> -dir <data_dir>
```

##### Command-line Arguments

- `-em_z`, `--embed_size`: Embedding size for word vectors (default: 32).
- `-hd_z`, `--hidden_size`: Hidden size for LSTM/GRU/RNN cells (default: 512).
- `-lr`, `--learning_rate`: Learning rate (default: 0.001).
- `-cell`, `--cell_type`: Type of recurrent cell (default: 'RNN'). Choices: "LSTM", "GRU", "RNN".
- `-n_l`, `--num_layers`: Number of stacked LSTM/GRU/RNN layers (default: 1).
- `-dp`, `--dropout`: Dropout rate for regularization (default: 0).
- `-0`, `--optimizer`: Optimizer used for training (default: 'ADAM').
- `-e`, `--epochs`: Number of epochs to train the network (default: 5).
- `-tfr`, `--teacher_forcing_ratio`: teacher_forcing_ratio (default: 0.5). 
- `-m_l`, `--max_length`: Maximum length (default: 50).
- `-dir`, `--data_dir`: Directory path containing the training dataset **required**

**Note**: Replace `<embed_size>`, `<hidden_size>`, `<learning_rate>`, and other placeholders with appropriate values.



## Content overview:

There are four folders in the repository. Following are the contents of the folder.

### NLG model with attention

This folder contains the functions that can be used to train a seq2seq model with an attention mechanism to perform the transliteration task given in assignment 3. ```train_model.py``` can be used to run the model.
   
### NLG model without attention

Here, you'll find functions for training a seq2seq model without an attention mechanism, and also for the transliteration task specified in assignment 3. Similar to the previous folder, you can use train_model.py to initiate the model training process.

### Notebook

The notebook folder contains the file used to conduct sweeps for questions 2 and 5. This notebook provides insights into the experimental setup and results analysis.

### prediction_attention

In this folder, you'll discover a PDF file comprising the predictions generated by the attention-based model. These predictions offer a glimpse into the model's performance and its transliteration capabilities.
