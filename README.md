# Null Subject Analysis Project
Project that aims to study the performance of the state-of-the-art translation models when dealing with pro-drop languages

## Requirements

* Python 3.6 (or higher)
* PyTorch 1.2 (or higher)
* For training models, you will need an NVIDIA GPU

## Install Fairseq

In order to get Fairseq, run the following commands (upgrade pip before):

``` 
git clone https://github.com/pytorch/fairseq 
cd fairseq
pip install --editable ./ 
```

## Install NVIDIA's apex library
Install NVIDIA’s apex library for faster training. It requires CUDA and CUDA toolkit installed
```
git clone https://github.com/NVIDIA/apex
cd apex
pip install -v --no-cache-dir --global-option="--cpp_ext" --global-option="--cuda_ext" \
  --global-option="--deprecated_fused_adam" --global-option="--xentropy" \
  --global-option="--fast_multihead_attn" ./
```

## Dataset

For training and testin. download the EUROPAL parallel corpus from here:
https://www.statmt.org/europarl/
