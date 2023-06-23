# Bangla Named Entity Recognition

This repository contains a Python script for performing Named Entity Recognition (NER) on Bangla text using a pre-trained model from the Flair library.

## Approach

The approach used in this project is to leverage a pre-trained NER model provided by the Flair library. The model was originally trained on the OntoNotes dataset in English, so its performance on Bangla text may not be optimal. Nevertheless, this approach provides a starting point for future improvements, such as training a custom model on a Bangla NER dataset.

## Usage

To run the script and perform NER on the sample sentence, simply run:

```bash
python ner_predict.py
