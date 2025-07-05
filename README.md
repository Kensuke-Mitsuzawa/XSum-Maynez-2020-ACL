# What's This Repository For?

This repository aims to reproduce the findings of the paper "On Faithfulness and Factuality in Abstractive Summarization."

The original project, published in 2020, is frequently cited even in 2025. However, its models, dataset resources, and package versions are poorly maintained. This repository unifies resources from multiple repositories and provides clear procedures for reproduction.

The paper reference is:

```

@inproceedings{maynez-etal-2020-faithfulness,
title = "On Faithfulness and Factuality in Abstractive Summarization",
author = "Maynez, Joshua  and
Narayan, Shashi  and
Bohnet, Bernd  and
McDonald, Ryan",
booktitle = "Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics",
month = jul,
year = "2020",
address = "Online",
publisher = "Association for Computational Linguistics",
url = "[https://aclanthology.org/2020.acl-main.173/](https://aclanthology.org/2020.acl-main.173/)",
doi = "10.18653/v1/2020.acl-main.173",
}

```

# Links to Resources

## XSum Dataset

The [XSum dataset](https://github.com/EdinburghNLP/XSum) is not openly available. Users who wish to use the dataset must reproduce it themselves. However, the original codebase is significantly outdated, making reproduction challenging.

Fortunately, a compatible version of the dataset is available on [HuggingFace Datasets](https://huggingface.co/datasets/shalinik/xsum).


## Annotated XSum Hallucination Dataset

The [dataset](https://github.com/google-research-datasets/xsum_hallucination_annotations) contains annotated data for generated summaries but does not include the original article text.

## Models

The original paper, `maynez-etal-2020-faithfulness`, references several summarization models.

### TRANS2S and BERTS2S

These are BERT-based models from the paper by [Sascha Rothe et al., 2020](https://direct.mit.edu/tacl/article/doi/10.1162/tacl_a_00313/96450/Leveraging-Pre-trained-Checkpoints-for-Sequence).

```

@article{10.1162/tacl\_a\_00313,
author = {Rothe, Sascha and Narayan, Shashi and Severyn, Aliaksei},
title = {Leveraging Pre-trained Checkpoints for Sequence Generation Tasks},
journal = {Transactions of the Association for Computational Linguistics},
volume = {8},
pages = {264-280},
year = {2020},
month = {06},
issn = {2307-387X},
doi = {10.1162/tacl\_a\_00313},
url = {[https://doi.org/10.1162/tacl](https://doi.org/10.1162/tacl)\_a\_00313},
eprint = {[https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl](https://direct.mit.edu/tacl/article-pdf/doi/10.1162/tacl)\_a\_00313/1923422/tacl\_a\_00313.pdf},
}

```

The original model, developed with TensorFlow (as of 2020), is hosted on [Kaggle](https://www.kaggle.com/models/google/bertseq2seq/TensorFlow1/roberta24-bbc/1). However, due to outdated TensorFlow package versions (requiring CUDA 10), running this model in current computational environments (as of 2025) is challenging.

Fortunately, a compatible trained model, based on PyTorch, is available on [HuggingFace](https://huggingface.co/google/roberta2roberta_L-24_bbc).


### RNN-based Seq2Seq

Out of scope for this repository.

### Topic-aware Convolutional Seq2Seq

Out of scope for this repository.
