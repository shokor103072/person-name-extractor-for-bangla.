from flair.models import SequenceTagger
from flair.data import Sentence

def load_model_and_predict(sentence_text):
    # Load the pre-trained NER model
    tagger = SequenceTagger.load("flair/ner-english-ontonotes-large")

    # Create a sentence
    sentence = Sentence(sentence_text)

    # Predict the NER tags
    tagger.predict(sentence)

    # Return the sentence with predicted tags
    return sentence.to_tagged_string()

if __name__ == "__main__":
    sentence_text = "আব্দুর রহিম নামের কাস্টমারকে একশ টাকা বাকি দিলাম"
    tagged_sentence = load_model_and_predict(sentence_text)
    print(tagged_sentence)
