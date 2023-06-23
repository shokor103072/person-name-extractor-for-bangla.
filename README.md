# Bangla Named Entity Recognition
This application is a Named Entity Recognition (NER) tool that is capable of identifying proper nouns such as names of people, locations, organizations, and other entities from the input text. It utilizes the pre-trained NER model from Flair, specifically the `flair/ner-english-ontonotes-large` model, to make predictions.

## Dependencies
This application uses the following libraries:

- `streamlit`
- `flair`
## Installation
Before running the application, you need to install the required libraries. You can install all of them at once using the following command:

```
pip install -r requirements.txt
```
## Usage
1. Run the application with the following command:
```
streamlit run ner_predict.py
```
2. Open your browser and go to ```http://localhost:8501.```

3. In the application, enter a sentence in the text input field.

4. Click on the 'Predict' button. The application will display the sentence with identified entities.

## Functionality
The main functions of the application are:

- `load_model()`: This function loads the pre-trained NER model from Flair.
- `predict(sentence_text, model)`: This function receives the user input text and the loaded model, then returns the sentence with the predicted NER tags.
## Model
The model used in this application is `flair/ner-english-ontonotes-large`, a large NER model pre-trained on the English OntoNotes dataset by Flair.
