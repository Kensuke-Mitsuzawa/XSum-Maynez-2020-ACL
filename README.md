# What's this?

This repository is for reproducing "On Faithfulness and Factuality in Abstractive Summarization".
The original project is relatively old and poorly managed. 
The codebase resources and dataset resources are scattered over multiple repositories, hence huge pain of reproducing the result.
Hence, this repository unifies multiple repositories and clearly indicates the reproduction procedures.

The reference is the following paper.

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
    url = "https://aclanthology.org/2020.acl-main.173/",
    doi = "10.18653/v1/2020.acl-main.173",
}
```

# Mandatory Repositories

## XSum Dataset

https://github.com/Kensuke-Mitsuzawa/XSum/tree/master/XSum-Dataset

The original dataset is not open.
The repository indicates the procedure to reproduce the dataset.

## Annotaed XSum Hallucination Dataset

https://github.com/Kensuke-Mitsuzawa/xsum_hallucination_annotations

The repository contains the annotaed data for the generated summaries.
However, it does not contain the original article text.

## TCONVS2S

https://github.com/Kensuke-Mitsuzawa/XSum/

The model name `TCONVS2S` (Topic-aware Convolutional Sequence to Sequence model) is in this repository. 
