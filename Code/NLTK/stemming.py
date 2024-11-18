import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
nltk.download('punkt')
ps = PorterStemmer()
text = "Aditya is running very faster because he is eagerly waiting to meet his mother."
words = word_tokenize(text)
stemmed_words = [ps.stem(word) for word in words]
print("Original Words:", words)
print("Stemmed Words:", stemmed_words)
