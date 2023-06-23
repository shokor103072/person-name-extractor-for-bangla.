import streamlit as st
from flair.models import SequenceTagger
from flair.data import Sentence

@st.cache(allow_output_mutation=True)
def load_model():
    return SequenceTagger.load("flair/ner-english-ontonotes-large")

def predict(sentence_text, model):
    sentence = Sentence(sentence_text)
    model.predict(sentence)
    return sentence.to_tagged_string()

model = load_model()

st.title('Bangla Named Entity Recognition')

sentence_text = st.text_input('Enter a sentence')

if st.button('Predict'):
    tagged_sentence = predict(sentence_text, model)
    st.write(tagged_sentence)
