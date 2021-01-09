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

# Dataset

For training and testin. download the EUROPAL parallel corpus from here:
https://www.statmt.org/europarl/

# Data preparation

The data_preparation.sh scripts performs the following steps on the corpus:

* download of the MOSES tokenizer script; tokenization of the whole corpus
* download of the BPE scripts; learning and applying BPE on the corpus

```
./data_preparation.sh setimes.en-mk.mk.txt setimes.en-mk.en.txt
```

After that the corpus is split into training, development and test set:

```
./split_dataset corpus.clean.bpe.32000.mk corpus.clean.bpe.32000.en
```

After that the fairseq tool can be invoked to preprocess the corpus:

```
fairseq preprocess -sourcelang mk -targetlang en -trainpref train/train \
                   -validpref dev/dev -testpref test/test -thresholdsrc 3 \
                   -thresholdtgt 3 -destdir model-data
```

# Training

After the preprossing steps the model can be trained.

```
CUDA_VISIBLE_DEVICES=0 fairseq-train  \   
                                    data-bin/iwslt14.tokenized.de-en \     
                                     --arch transformer_iwslt_de_en \
                                     --share-decoder-input-output-embed \     
                                     --optimizer adam \
                                     --adam-betas '(0.9, 0.98)' \
                                     --clip-norm 0.0     \
                                     --lr 5e-4 \
                                     --lr-scheduler inverse_sqrt \
                                     --warmup-updates 4000     \
                                     --dropout 0.3 \
                                     --weight-decay 0.0001  \   
                                     --criterion label_smoothed_cross_entropy \
                                     --label-smoothing 0.1     \
                                     --max-tokens 4096     \
                                     --eval-bleu     \
                                     --eval-bleu-args '{"beam": 5, "max_len_a": 1.2, "max_len_b": 10}' \     
                                     --eval-bleu-detok moses     \
                                     --eval-bleu-remove-bpe     \
                                     --eval-bleu-print-samples   \  
                                     --best-checkpoint-metric bleu \
                                     --maximize-best-checkpoint-metric \ 
                                     --num-workers 0 \
                                     --max-epoch 3\

```

# Calculating the BLEU-score

```
fairseq-generate data-bin/iwslt14.tokenized.de-en     \
                                     --path checkpoints/checkpoint_best.pt \    
                                     --batch-size 128 --beam 5 \
                                     --remove-bpe \
                                     --num-workers 0
```
