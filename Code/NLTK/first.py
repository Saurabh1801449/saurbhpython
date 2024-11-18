
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt_tab')
nltk.download('punkt')

text = "Hello Aditya! Welcome to the world of Natural Language Processing. This is a simple NLTK demo."

sentences = sent_tokenize(text)
print("Sentence Tokenization:", sentences)

words = word_tokenize(text)
print("Word Tokenization:", words)
